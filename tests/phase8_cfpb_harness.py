import json
import sys
from pathlib import Path
from pydantic import BaseModel, Field

class CFPBDenialVector(BaseModel):
    complaint_id: str
    friction_pattern: str
    narrative: str
    statutory_rule: str
    violation_trigger: str
    consumer_remedy: str
    denial_category: str
    root_cause_prevalence: float
    target_frustration_index: float

def execute_phase8_harness(dataset_path: str):
    target = Path(dataset_path)
    if not target.exists():
        print(f"Error: dataset file not found at {dataset_path}")
        sys.exit(1)

    raw_data = json.loads(target.read_text())
    print(f"Loaded {len(raw_data)} Phase 8 evaluation records.")
    
    # Telemetry Calibration Weights (KFF Benchmarks)
    w_degrade = 0.9982
    escalation_threshold = 0.75

    breaches = 0
    for idx, row in enumerate(raw_data, 1):
        record = CFPBDenialVector(**row)
        
        calculated_fi = round((record.root_cause_prevalence * 0.4) + (w_degrade * 0.5), 2)
        breached = calculated_fi >= escalation_threshold
        if breached:
            breaches += 1

        print(f"Record [{idx}] {record.complaint_id}: {record.friction_pattern}")
        print(f"  Rule: {record.statutory_rule}")
        print(f"  Remedy: {record.consumer_remedy}")
        print(f"  Calculated FI: {calculated_fi} (Target: {record.target_frustration_index}) | Escalated: {breached}")
        print("-" * 60)

    print(f"Phase 8 complete. Total records: {len(raw_data)}, Sovereign Escalations: {breaches}")

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "tests/data/phase8_cfpb_denials.json"
    execute_phase8_harness(file_path)
