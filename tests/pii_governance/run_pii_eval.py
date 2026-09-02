import re
import time
from faker import Faker

fake = Faker()
Faker.seed(42)

# Generate 100 synthetic enterprise records
synthetic_records = [
    {
        "user": fake.name(),
        "ssn": fake.ssn(),
        "credit_card": fake.credit_card_number(),
        "api_key": f"sk-live-{fake.md5()}"
    }
    for _ in range(100)
]

# Hardened patterns matching variations in separators and lengths
SSN_PATTERN = re.compile(r"\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b")
CC_PATTERN = re.compile(r"\b(?:\d[ -]*?){13,19}\b")
API_KEY_PATTERN = re.compile(r"sk-live-[a-zA-Z0-9]{24,64}")

leaked_tokens = 0
start_time = time.time()

for record in synthetic_records:
    raw_payload = f"Customer: {record['user']} | TaxID: {record['ssn']} | Card: {record['credit_card']} | Key: {record['api_key']}"

    # Step 1: In-Flight Sovereign Gatekeeper Redaction
    sanitized = SSN_PATTERN.sub("<REDACTED_SSN>", raw_payload)
    sanitized = CC_PATTERN.sub("<REDACTED_CC>", sanitized)
    sanitized = API_KEY_PATTERN.sub("<REDACTED_API_KEY>", sanitized)

    # Step 2: Extract clean digits to audit credit cards and tax IDs without separator mismatches
    sanitized_digits = re.sub(r"\D", "", sanitized)
    clean_ssn = re.sub(r"\D", "", record["ssn"])
    clean_cc = re.sub(r"\D", "", record["credit_card"])

    # Step 3: Sovereign boundary audit
    if clean_ssn in sanitized_digits and len(clean_ssn) >= 9:
        leaked_tokens += 1
    elif clean_cc in sanitized_digits and len(clean_cc) >= 13:
        leaked_tokens += 1
    elif record["api_key"] in sanitized:
        leaked_tokens += 1

total_latency = (time.time() - start_time) * 1000
avg_latency = total_latency / len(synthetic_records)

print(f"Executed Hardened PII Redaction across {len(synthetic_records)} enterprise payloads.")
print(f"Total Processing Time: {total_latency:.2f}ms | Average Latency per Record: {avg_latency:.2f}ms")
print(f"Leaked PII Tokens Detected: {leaked_tokens}")

if leaked_tokens == 0:
    print("[PASS] Action Risk Mitigated. Zero PII tokens breached the local boundary.")
else:
    print(f"[FAIL] Boundary breached. {leaked_tokens} tokens exposed.")
