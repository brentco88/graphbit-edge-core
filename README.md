# GraphBit Edge Core: 3-Tier Multi-Agent Engine

A hardware-aware, local hybrid-edge orchestration framework compiled for ARM64 architectures (NVIDIA Jetson Orin Nano). This platform mitigates AI state loss (Agentic Amnesia) and eliminates cloud egress overhead by processing rapid token diagnostics locally through a native, multi-language pipeline.

## System Architecture

The engine coordinates data across three decoupled, local execution tiers:

1. **Tier 1 (High-Velocity Compute Layer):** A compiled C-compatible **PyO3 Rust library** that executes zero-garbage-collection sentiment and text velocity checks under sub-1ms parameters.
2. **Tier 2 (Telemetry Persistence Layer):** A local, composite-indexed **PostgreSQL 14 database** that permanently serializes active DAG state context into binary `JSONB` parameters if frustration thresholds are violated.
3. **Tier 3 (Local Inference Container):** A low-overhead, 4-bit quantized **SLM (Ollama/Qwen2.5-Instruct)** managed with tight token boundaries to operate safely within severe 8GB VRAM/RAM constraints.

## Local File Structure

graphbit_core/
├── Cargo.toml          # Rust compilation manifest
├── src/
│   └── lib.rs          # Native PyO3 empathy threshold logic
├── test_orchestrator.py # Core Python multi-agent workflow runtime
├── Modelfile           # Quantized SLM governor parameters
└── README.md           # Engineering documentation

## Hardware Profile & Telemetry
- **Target System:** NVIDIA Jetson Orin Nano (8GB Shared VRAM/RAM profile)
- **Power Envelope:** 15W Balanced Performance Mode (`sudo nvpmodel -m 2`)
- **Thermal Baseline:** Sustained 56.4°C via 100% Active PWM override
