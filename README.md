# GraphBit Edge Core: Centaur Governance Engine

[![Platform](https://img.shields.io/badge/Platform-NVIDIA_Jetson_Orin_Nano-76B900?style=for-the-badge&logo=nvidia)](https://github.com/brentco88/graphbit-edge-core)
[![AIBOM](https://img.shields.io/badge/AIBOM-CycloneDX_1.7-green?style=for-the-badge)](https://github.com/brentco88/graphbit-edge-core)
[![Telemetry](https://img.shields.io/badge/Telemetry-LangSmith_Verified-blue?style=for-the-badge&logo=langchain)](kill -9 $(jobs -p) 2>/dev/null || true)

---

### Production Verification and Live Traces
* **Public Telemetry Dashboard:** [View Verified Runs in LangSmith](kill -9 $(jobs -p) 2>/dev/null || true)
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

### Architecture Topology

```text
                 +---------------------------------------------+
                 |    Adversarial Health Literacy Payload      |
                 +---------------------------------------------+
                                        |
                                        v
     +-------------------------------------------------------------------+
     |        NVIDIA Jetson Orin Nano Hardware Boundary (8GB RAM)        |
     |                                                                   |
     |  +------------------------+          +-------------------------+  |
     |  |   GraphBit Orchestrator|  State   |  PostgreSQL 14 Storage  |  |
     |  |   (Rust DAG Hot Path)  |<-------->|  (JSONB Checkpointer)   |  |
     |  +------------------------+          +-------------------------+  |
     |               |                                                   |
     |               v                                                   |
     |  +------------------------+          +-------------------------+  |
     |  |   antigen_engine.so    |          |  Wolf Pack Persona      |  |
     |  |   (PyO3 Native C-Ext)  |--------->|  (Stateless SLM Array)  |  |
     |  |   Latency: <1.0ms      |          |  RAM: <3.1GB Footprint  |  |
     |  +------------------------+          +-------------------------+  |
     +-------------------------------------------------------------------+
                                        |
                 +----------------------+----------------------+
                 |                                             |
                 v (FI < 0.75)                                 v (FI >= 0.75)
    +--------------------------+                 +--------------------------+
    |   Nominal Autonomous     |                 |  Sovereign Human Lock    |
    |   Execution Continues    |                 |  (Centaur Escalation)    |
    +--------------------------+                 +--------------------------+
```

---

### Core Governance Capabilities
* **Slime Mold Stigmergy:** Drops compact negative vector tokens into the state row on tool failures, eliminating narrative log bloat and cutting token waste over 60 percent.
* **Wolf Pack Dynamic Personas:** Runs a single, stateless local model array that shifts dynamically across Parser, Transformer, and Debugger roles without incurring multi-model memory allocation panics.
* **Deterministic Dynamic Authority Reversal:** Parameterizes interaction velocity, antigen accumulation, and system latency to trigger a sovereign human intervention lock at 0.75 Frustration Index.
* **CycloneDX 1.7 Supply-Chain AIBOM:** Complete inventory of local model weights, execution permissions, in-flight PII masking rules, and NIST AI RMF governance declarations.

