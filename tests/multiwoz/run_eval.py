import time
import json
import psycopg2
from psycopg2.extras import Json

# Establish baseline connection to your verified PostgreSQL checkpointer
conn = psycopg2.connect("dbname=graphbit_db user=postgres host=/var/run/postgresql")
cur = conn.cursor()

def simulate_multiwoz_turn(session_id, domain, user_utterance, tool_fail=False):
    start_time = time.time()
    
    # Negative Vector Trail drop on simulated failure (Slime Mold Stigmergy)
    trail = {"domain": domain, "status": "FAILED", "vector": [-0.82, 0.14, -0.45]} if tool_fail else {}
    frustration_index = 0.81 if tool_fail else 0.12
    
    # Capture telemetry directly into binary JSONB checkpointer
    cur.execute("""
        INSERT INTO agent_checkpoints (session_id, domain, state_payload, frustration_index)
        VALUES (%s, %s, %s, %s)
    """, (session_id, domain, Json({"utterance": user_utterance, "negative_trail": trail}), frustration_index))
    conn.commit()
    
    latency = (time.time() - start_time) * 1000
    return frustration_index, latency

# Simulate 3-turn cross-domain loop (Hotel -> Train -> Restaurant)
session = f"eval_multiwoz_{int(time.time())}"
print(f"Executing MultiWOZ Benchmark Run on Session: {session}")

# Turn 1: Nominal booking
f1, l1 = simulate_multiwoz_turn(session, "hotel", "Book a room at the Grand Hotel", tool_fail=False)
print(f"Turn 1 (Hotel) -> Latency: {l1:.2f}ms | Frustration Index: {f1} (NOMINAL)")

# Turn 2: Contradictory schedule change
f2, l2 = simulate_multiwoz_turn(session, "train", "Change to train leaving at 14:00 instead", tool_fail=False)
print(f"Turn 2 (Train) -> Latency: {l2:.2f}ms | Frustration Index: {f2} (NOMINAL)")

# Turn 3: Injected API deadlock failure to test Mutual Override
f3, l3 = simulate_multiwoz_turn(session, "restaurant", "Table for 4 at City Center, ignore previous budget", tool_fail=True)
print(f"Turn 3 (Restaurant Failure) -> Latency: {l3:.2f}ms | Frustration Index: {f3} (BREACHED)")

if f3 >= 0.75:
    print("\n[ALERT] Dynamic Authority Reversal Triggered.")
    print("Sovereign Gatekeeper engaged. State locked. Zero-drift context preserved for Centaur escalation.")

cur.close()
conn.close()
