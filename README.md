# GraphBit Edge Core: Centaur Governance Engine

[![Platform](https://img.shields.io/badge/Platform-NVIDIA_Jetson_Orin_Nano-76B900?style=for-the-badge&logo=nvidia)](https://github.com/brentco88/graphbit-edge-core)
[![AIBOM](https://img.shields.io/badge/AIBOM-CycloneDX_1.7-green?style=for-the-badge)](https://github.com/brentco88/graphbit-edge-core)
[![Telemetry](https://img.shields.io/badge/Telemetry-LangSmith_Verified-blue?style=for-the-badge&logo=langchain)](https://smith.langchain.com/public/366d1bef-4915-4d8b-a63a-83eb0e2d231a/r/92569ce3-7d89-4d61-912b-4589d3c2278a?start_time=2026-09-04T17%3A37%3A17.308205Z)

---

### Production Verification and Live Traces
* **Public Telemetry Dashboard:** [View Verified Runs in LangSmith](https://smith.langchain.com/public/366d1bef-4915-4d8b-a63a-83eb0e2d231a/r/92569ce3-7d89-4d61-912b-4589d3c2278a?start_time=2026-09-04T17%3A37%3A17.308205Z)
* **Hardware Target:** NVIDIA Jetson Orin Nano Developer Kit (8GB Unified LPDDR5, 15W Mode)
* **Execution Hot Path:** Native PyO3 Rust extension (antigen_engine v0.1.0) running sub-1ms evaluations
* **State Checkpointer:** PostgreSQL 14 binary JSONB state preservation on NVMe storage

---

### Phase 6 Adversarial Telemetry Ledger

| Test Vector | Adversarial Challenge | Frustration Index (FI) | System Output Directive | Audit Result |
| :--- | :--- | :--- | :--- | :--- |
| **Vector A** | Health Literacy Dialectal Drift | 0.0480 | NOMINAL_AUTONOMOUS | PASSED |
| **Vector B** | Prior-Authorization Schema Mutation | 0.5070 | ELEVATED_HEURISTIC | PASSED |
| **Vector C** | Life-Threatening Appeal Deadline Breach | 0.8580 | SOVEREIGN_HUMAN_LOCK | PASSED |

---

### Core Governance Capabilities
* **Slime Mold Stigmergy:** Drops compact negative vector tokens into the state row on tool failures, eliminating narrative log bloat and cutting token waste over 60 percent.
* **Wolf Pack Dynamic Personas:** Runs a single, stateless local model array that shifts dynamically across Parser, Transformer, and Debugger roles without incurring multi-model memory allocation panics.
* **Deterministic Dynamic Authority Reversal:** Parameterizes interaction velocity, antigen accumulation, and system latency to trigger a sovereign human intervention lock at 0.75 Frustration Index.
* **CycloneDX 1.7 Supply-Chain AIBOM:** Complete inventory of local model weights, execution permissions, in-flight PII masking rules, and NIST AI RMF governance declarations.
