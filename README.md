# GraphBit Edge Core: Bio-Inspired Multi-Agent Orchestration Engine

Deterministic, edge-native agentic runtime engineered for the 8GB NVIDIA Jetson Orin Nano. Built with a compiled Rust core (PyO3) and a PostgreSQL 14 binary JSONB checkpointer to prevent agent amnesia, eliminate token loops, and enforce deterministic Human-in-the-Loop governance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hardware Target](https://img.shields.io/badge/Hardware-NVIDIA%20Jetson%20Orin%20Nano%20(8GB)-green.svg)](https://www.nvidia.com)
[![Specification](https://img.shields.io/badge/Compliance-CycloneDX%201.7%20AIBOM-blue.svg)](https://cyclonedx.org)
[![Governance](https://img.shields.io/badge/NIST-AI%20RMF%201.0-orange.svg)](https://www.nist.gov)

---

## Architectural Moat: Stigmergy & Sovereign Gatekeeping

Enterprise multi-agent pipelines collapse into recursive token loops when contradictory user requests trigger tool failures. GraphBit rejects verbose narrative text logging in favor of biological stigmergy and mathematical authority gating.

```text
[ User Input / Client Telemetry ]
               │
               ▼
[ Sovereign Gatekeeper: In-Flight PII Redaction ] ──(0.03ms / Zero Leak)
               │
               ▼
[ Blackboard Architecture: PostgreSQL 14 JSONB Checkpointer ]
         ▲                     ▲                     ▲
         │                     │                     │
   [ Parser Node ]       [ Transformer Node ]   [ Debugger Node ]
    (Wolf Pack)             (Wolf Pack)            (Wolf Pack)
               │
               ▼
[ PyO3 Rust Telemetry Thread: Frustration Index Engine ]
               │
         ┌─────┴─────────────────────────┐
         │                               │
[ FI < 0.75: Nominal Execution ]   [ FI >= 0.75: Sovereign Overwrite ]
                                                 │
                                                 ▼
                                    [ Mutual Override Engaged ]
                                    [ State Row Locked in 1.32ms ]
                                    [ Zero-Drift Context to Centaur ]
