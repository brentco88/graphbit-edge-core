use std::error::Error;
use std::fs::File;
use std::io::Write;

fn main() -> Result<(), Box<dyn Error>> {
    let file_path = "generated/telco_churn_mock_data.csv";
    let mut file = File::create(file_path)?;

    writeln!(
        file,
        "customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn"
    )?;

    let contracts = vec!["Month-to-month", "One year", "Two year"];
    let payment_methods = vec![
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)",
    ];
    let internet_services = vec!["DSL", "Fiber optic", "No"];
    let yes_no = vec!["Yes", "No"];

    for i in 1..=100 {
        let customer_id = format!("{:04}-XXXXX", i);
        let gender = if i % 2 == 0 { "Male" } else { "Female" };
        let senior_citizen = if i % 7 == 0 { 1 } else { 0 };
        let partner = yes_no[i % 2];
        let dependents = yes_no[(i % 3 == 0) as usize];
        let tenure = (i * 7) % 73;
        let phone_service = if i % 10 == 0 { "No" } else { "Yes" };
        let multiple_lines = if phone_service == "No" { "No phone service" } else { yes_no[i % 2] };
        let internet_service = internet_services[i % 3];
        let (online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies) = 
            if internet_service == "No" {
                ("No internet service", "No internet service", "No internet service", "No internet service", "No internet service", "No internet service")
            } else {
                (yes_no[i % 2], yes_no[(i + 1) % 2], yes_no[i % 2], yes_no[(i + 1) % 2], yes_no[i % 2], yes_no[(i + 1) % 2])
            };
        let contract = contracts[i % 3];
        let paperless_billing = yes_no[(i + 2) % 2];
        let payment_method = payment_methods[i % 4];
        let base_charge = match internet_service {
            "Fiber optic" => 85.0,
            "DSL" => 45.0,
            _ => 20.0,
        };
        let monthly_charges = base_charge + (i % 30) as f64;
        let total_charges = monthly_charges * (tenure as f64).max(1.0);
        let churn = if contract == "Month-to-month" && tenure < 12 && i % 2 == 0 { "Yes" } else { "No" };

        writeln!(
            file,
            "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{:.2},{:.2},{}",
            customer_id, gender, senior_citizen, partner, dependents, tenure,
            phone_service, multiple_lines, internet_service, online_security,
            online_backup, device_protection, tech_support, streaming_tv,
            streaming_movies, contract, paperless_billing, payment_method,
            monthly_charges, total_charges, churn
        )?;
    }
    println!("Successfully generated mock CSV with 100 rows.");
    Ok(())
}
