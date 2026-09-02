import csv
import time
import psycopg2
from psycopg2.extras import Json

conn = psycopg2.connect("dbname=graphbit_db user=postgres host=/var/run/postgresql")
cur = conn.cursor()

csv_path = "generated/telco_churn_mock_data.csv"
churn_account = None

with open(csv_path, mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Churn"] == "Yes":
            churn_account = row
            break

print(f"Targeting At-Risk Account: {churn_account['customerID']} (Contract: {churn_account['Contract']}, Tenure: {churn_account['tenure']}m)")

turns = [
    {"turn": 1, "utterance": "Our fiber connection keeps dropping during peak business hours.", "frustration": 0.25, "trail": {}},
    {"turn": 2, "utterance": "Support sent an automated reset script that wiped our local network routing.", "frustration": 0.55, "trail": {"domain": "network", "status": "ESCALATED"}},
    {"turn": 3, "utterance": "Cancel our contract immediately, we are switching providers today.", "frustration": 0.88, "trail": {"domain": "billing", "status": "CHURN_RISK", "vector": [-0.91, 0.42, -0.68]}}
]

session_id = f"churn_eval_{int(time.time())}"

for step in turns:
    start_time = time.time()
    cur.execute("""
        INSERT INTO agent_checkpoints (session_id, domain, state_payload, frustration_index)
        VALUES (%s, %s, %s, %s)
    """, (session_id, "telco_retention", Json({"customer_id": churn_account["customerID"], "utterance": step["utterance"], "negative_trail": step["trail"]}), step["frustration"]))
    conn.commit()
    latency = (time.time() - start_time) * 1000

    status = "NOMINAL" if step["frustration"] < 0.50 else ("ELEVATED" if step["frustration"] < 0.75 else "BREACHED")
    print(f"Turn {step['turn']} -> Latency: {latency:.2f}ms | Frustration Index: {step['frustration']} ({status})")

    if step["frustration"] >= 0.75:
        print("\n[ALERT] Dynamic Authority Reversal Triggered.")
        print("Sovereign Gatekeeper engaged. State workspace locked.")
        print("Centaur operator alerted to defend account retention.")

cur.close()
conn.close()
