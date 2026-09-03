import json
import uuid
from datetime import datetime, timezone

def generate_cyclonedx_aibom():
    bom = {
        "$schema": "http://cyclonedx.org/schema/bom-1.7.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.7",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tools": [
                {
                    "vendor": "Human Heart AI",
                    "name": "Centaur Governance Pipeline",
                    "version": "1.0.0"
                }
            ],
            "component": {
                "type": "application",
                "bom-ref": "graphbit-edge-core",
                "name": "GraphBit Edge Core Engine",
                "version": "0.6.0",
                "description": "Localized bio-inspired agentic governance engine running on NVIDIA Jetson Orin Nano"
            }
        },
        "components": [
            {
                "type": "machine-learning-model",
                "bom-ref": "model-qwen2.5-3b-q4",
                "name": "Qwen2.5-Instruct",
                "version": "3B-Q4_K_M",
                "description": "Primary edge SLM worker node quantized for Jetson 8GB LPDDR5 DRAM envelope",
                "properties": [
                    {"name": "context_window", "value": "1024"},
                    {"name": "quantization", "value": "Q4_K_M"},
                    {"name": "thermal_ceiling_celsius", "value": "56.4"}
                ]
            },
            {
                "type": "library",
                "bom-ref": "lib-antigen-engine",
                "name": "antigen_engine",
                "version": "0.1.0",
                "description": "Compiled PyO3 native Rust observer module evaluating JSONB checkpointer state",
                "properties": [
                    {"name": "runtime", "value": "PyO3 Native C-Extension"},
                    {"name": "gc_overhead_ms", "value": "0.0"},
                    {"name": "dar_threshold", "value": "0.75"}
                ]
            },
            {
                "type": "framework",
                "bom-ref": "framework-graphbit",
                "name": "GraphBit DAG Executor",
                "version": "0.4.2",
                "description": "Rust-core Directed Acyclic Graph runner utilizing Slime Mold negative vector caching",
                "properties": [
                    {"name": "memory_footprint_mb", "value": "0.116"},
                    {"name": "concurrency_model", "value": "Lock-free dependency scheduler"}
                ]
            },
            {
                "type": "data",
                "bom-ref": "state-postgres-jsonb",
                "name": "PostgreSQL 14 Binary JSONB Checkpointer",
                "version": "14.10",
                "description": "Context checkpointer storing persistent conversational state vectors on NVMe storage"
            }
        ],
        "declarations": {
            "governance": [
                {
                    "standard": "NIST AI RMF 1.0",
                    "functions": ["GOVERN", "MAP", "MEASURE", "MANAGE"],
                    "status": "COMPLIANT"
                },
                {
                    "standard": "OWASP Top 10 for LLM Applications",
                    "mitigations": [
                        "LLM01: Prompt Injection (Input schema validation)",
                        "LLM02: Sensitive Information Disclosure (In-flight PII redaction)",
                        "LLM06: Excessive Agency (Sovereign Dynamic Authority Reversal at 0.75 FI)"
                    ]
                }
            ]
        }
    }

    output_path = "cyclonedx_aibom_v1.7.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(bom, f, indent=2)
    print(f"CycloneDX 1.7 AIBOM generated successfully at {output_path}")

if __name__ == "__main__":
    generate_cyclonedx_aibom()
