use pyo3::prelude::*;

#[pyfunction]
fn calculate_frustration_index(reply_velocity_seconds: f64, message_length: usize) -> PyResult<i32> {
    let mut score = 0;

    // Condition 1: High velocity short replies indicate an intense frustration profile
    if reply_velocity_seconds < 3.0 && message_length < 15 {
        score += 45;
    } else if reply_velocity_seconds < 6.0 {
        score += 20;
    }

    // Condition 2: Escalating response size indicates complex unresolved operational drift
    if message_length > 300 {
        score += 35;
    }

    Ok(score)
}

#[pymodule]
fn frustration_monitor(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_frustration_index, m)?)?;
    Ok(())
}
