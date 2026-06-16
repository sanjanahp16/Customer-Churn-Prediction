import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def clean_and_split_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    
    # Drop CustomerID as it isn't a feature
    df = df.drop(columns=['customerID'], errors='ignore')
    
    # TotalCharges contains blank spaces; convert to NaN and fill with 0
    df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
    df['TotalCharges'] = df['TotalCharges'].astype(float).fillna(0)
    
    # Map target variable 'Churn' to 1 (Yes) and 0 (No)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Separate features and target
    X = df.drop(columns=['Churn'])
    y = df['Churn']
    
    # Identify column types
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    cat_cols = [col for col in X.columns if col not in num_cols]
    
    # Create a preprocessor pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
        ]
    )
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Fit and transform
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)
    
    # Get feature names for later use in Feature Importance
    cat_encoder = preprocessor.named_transformers_['cat']
    encoded_cat_cols = cat_encoder.get_feature_names_out(cat_cols).tolist()
    feature_names = num_cols + encoded_cat_cols
    
    return X_train_transformed, X_test_transformed, y_train, y_test, preprocessor, feature_names