import os
import glob
import json
import psycopg2
from pydantic import BaseModel, Field

class StatePayload(BaseModel):
    session_id: str
    socratic_mode: str = Field(default="standard")
    node_role: str = Field(default="chaser")
    user_query: str
    repetitive_query_count: int = 0

class HardwareTelemetryProbePython:
    def __init__(self):
        base_dir = "/sys/bus/i2c/drivers/ina3221/1-0040/hwmon"
        matches = glob.glob(os.path.join(base_dir, "hwmon*"))
        self.hwmon_base_path = matches[0] if matches else "/sys/bus/i2c/drivers/ina3221/1-0040/hwmon/hwmon0"

    def read_power_watts(self) -> float:
        in1_file = os.path.join(self.hwmon_base_path, "in1_input")
        curr1_file = os.path.join(self.hwmon_base_path, "curr1_input")
        
        try:
            with open(in1_file, "r") as f:
                voltage_mv = float(f.read().strip())
            with open(curr1_file, "r") as f:
                current_ma = float(f.read().strip())
            return (voltage_mv * current_ma) / 1000000.0
        except Exception:
            return 11.4  # Hardware baseline fallback (15W power mode)

    def calculate_step_telemetry(self, latency_ms: float, carbon_factor: float):
        power_watts = self.read_power_watts()
        duration_sec = latency_ms / 1000.0
        energy_joules = power_watts * duration_sec
        estimated_carbon_kg = energy_joules * carbon_factor
        return power_watts, energy_joules, estimated_carbon_kg

def run_phase3_pipeline(raw_state: dict, db_conn):
    state = StatePayload.model_validate(raw_state)
    
    pqa_triggered = False
    warning_ticket = None
    
    if state.socratic_mode == "strategic":
        state.node_role = "ambusher"
        pqa_triggered = True
    elif state.repetitive_query_count > 3:
        warning_ticket = {
            "event": "VENDING_MACHINE_PATTERN_DETECTED",
            "message": "High query frequency detected without structural synthesis. Consider Strategic Mode."
        }
        pqa_triggered = True

    probe = HardwareTelemetryProbePython()
    latency_ms = raw_state.get("latency_ms", 142.8)
    carbon_factor = 0.000115

    power_watts, energy_joules, estimated_carbon_kg = probe.calculate_step_telemetry(
        latency_ms, carbon_factor
    )

    telemetry_record = {
        "frustration_index": raw_state.get("frustration_index", 0.42),
        "system_latency_ms": latency_ms,
        "power_draw_watts": power_watts,
        "energy_consumed_joules": energy_joules,
        "estimated_carbon_kg": estimated_carbon_kg,
        "pqa_score": 1.0 if pqa_triggered else 0.0,
        "active_socratic_mode": state.socratic_mode,
        "warning_ticket": warning_ticket
    }

    with db_conn.cursor() as cursor:
        cursor.execute(
            """
            UPDATE dag_state_store 
            SET state_payload = %s, telemetry_context = %s, updated_at = NOW()
            WHERE session_id = %s;
            """,
            (json.dumps(state.model_dump()), json.dumps(telemetry_record), state.session_id)
        )
    db_conn.commit()

    return {"state": state.model_dump(), "telemetry": telemetry_record}
