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

### 🛡️ Adversarial Stress Testing & Governance
Relying on base model alignment is an enterprise anti pattern. To validate system boundaries, this framework undergoes automated security verification using a surgically abliterated open source model. System compliance is strictly enforced at the routing and orchestration layers. 

For the comprehensive technical breakdown including latency, cost optimization, and human fallback thresholds, read the [Adversarial Harness EPIC Specification](docs/architecture/adversarial-harness-epic.md).

## Technical Appendix: Wabi-Sabi Vulnerability & Telemetry Manifest

### 1. State Store I/O Contention
* **Vulnerability:** Polymorphic worker nodes utilize blocking synchronous writes to a centralized PostgreSQL checkpointer. High-velocity execution loops induce severe I/O bottlenecks and transaction serialization failures under intense multi-agent concurrency.
* **Mishap Path:** Multiple micro-agents writing task states and vector trails simultaneously exhaust the database connection pool on ARM architectures before the PyO3 Rust thread can compute the Frustration Index.
* **Mitigation:** Strict database connection pool caps paired with an automated Human-in-the-Loop circuit breaker that fires the moment transaction exceptions persist beyond a 1500ms fence window.

### 2. Context Inflation Tax
* **Vulnerability:** Worker nodes are stateless to preserve the unified memory footprint of the 8GB Jetson Orin Nano. The architecture suffers from cold-start amnesia during nested loop iterations.
* **Mishap Path:** Small language models (Qwen-3B / Llama 3.2) consume 250 tokens per activation solely on prompt bootstrapping and macro-objective alignment, causing acute processing latency spikes and resource degradation.
* **Mitigation:** Context optimization through highly compressed, binary encoded global state variables injected directly into the active DAG execution node.

### 3. Cascading Schema Fragility
* **Vulnerability:** Data exchanges between decoupled nodes rely entirely on rigid, deterministic structured JSON outputs.
* **Mishap Path:** Minor token truncation or minor quantization variations within local SLM inference introduce minute formatting anomalies, corrupting the shared blackboard state and causing immediate downstream graph serialization failures.
* **Mitigation:** Native runtime type-validation via Pydantic schemas enforced strictly at the entry and exit perimeter of every graph node node to preemptively block context poisoning.

### 4. Edge-to-Cloud Asynchronous Race Conditions
* **Vulnerability:** The hybrid routing engine splits processing logic between localized edge hardware and serverless cloud bursting targets.
* **Mishap Path:** Network connectivity degradation causes local node tracking timeouts. A local process may write an execution failure to the checkpointer while a remote cloud node is still executing a complex Socratic task, inducing conflicting concurrent state mutations when the delayed payload arrives.
* **Mitigation:** Implementation of immutable transaction IDs tied to composite keys within the PostgreSQL ledger, establishing automated authority reversal rules for asynchronous responses.
