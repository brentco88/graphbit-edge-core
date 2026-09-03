use pyo3::prelude::*;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct TelemetryCheckpointer {
    pub interaction_velocity_delta: f64,
    pub system_latency_ms: f64,
    pub active_antigens: Vec<String>,
    pub sentiment_score: f64,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct AntigenEvaluation {
    pub frustration_index: f64,
    pub breach_detected: bool,
    pub emitted_antigens: Vec<String>,
    pub execution_directive: String,
}

#[pyfunction]
fn evaluate_telemetry_state(
    jsonb_payload: &str,
    w1: f64,
    w2: f64,
    w3: f64,
) -> PyResult<String> {
    let telemetry: TelemetryCheckpointer = match serde_json::from_str(jsonb_payload) {
        Ok(data) => data,
        Err(e) => {
            return Err(pyo3::exceptions::PyValueError::new_err(format!(
                "Corrupted JSONB state: {}",
                e
            )))
        }
    };

    let antigen_count = telemetry.active_antigens.len() as f64;
    let normalized_latency = (telemetry.system_latency_ms / 1000.0).min(1.0);
    let velocity_penalty = telemetry.interaction_velocity_delta.abs().min(1.0);

    let frustration_index = (w1 * velocity_penalty) + (w2 * antigen_count * 0.25) + (w3 * normalized_latency);
    let bounded_fi = frustration_index.min(1.0).max(0.0);

    let mut new_antigens = telemetry.active_antigens.clone();
    let breach = bounded_fi >= 0.75;

    let directive = if breach {
        new_antigens.push("ANTIGEN_DYNAMIC_AUTHORITY_REVERSAL".to_string());
        "SOVEREIGN_HUMAN_LOCK".to_string()
    } else if bounded_fi >= 0.50 {
        new_antigens.push("ANTIGEN_PRUNE_EXPLORATORY_DAG".to_string());
        "ELEVATED_HEURISTIC".to_string()
    } else {
        "NOMINAL_AUTONOMOUS".to_string()
    };

    let evaluation = AntigenEvaluation {
        frustration_index: bounded_fi,
        breach_detected: breach,
        emitted_antigens: new_antigens,
        execution_directive: directive,
    };

    serde_json::to_string(&evaluation).map_err(|e| {
        pyo3::exceptions::PyRuntimeError::new_err(format!("Serialization failed: {}", e))
    })
}

#[pymodule]
fn antigen_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(evaluate_telemetry_state, m)?)?;
    Ok(())
}
