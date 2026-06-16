import joblib
import pandas as pd

def predict_single_customer(customer_dict):
    # Load Saved Model and Transformer Pipeline
    model = joblib.load('models/model.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    
    # Convert input dictionary into DataFrame row
    df_input = pd.DataFrame([customer_dict])
    
    # Process inputs
    processed_input = preprocessor.transform(df_input)
    
    # Predict Probability
    churn_probability = model.predict_proba(processed_input)[0][1]
    
    return round(float(churn_probability * 100), 2)