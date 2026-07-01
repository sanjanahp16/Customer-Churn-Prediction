# Customer Churn Prediction

## Overview
This project predicts whether a customer is likely to churn using Machine Learning.

## Features
- Customer churn prediction
- Streamlit web application
- Docker containerization
- Jenkins CI/CD pipeline

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker
- Jenkins
- Git & GitHub

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Docker

Build the image:

```bash
docker build -t customer-churn-app .
```

Run the container:

```bash
docker run -p 8501:8501 customer-churn-app
```