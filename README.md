# 🚀 Customer Churn Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red?logo=jenkins)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-black?logo=github)

---

# 📌 Project Overview

Customer Churn Prediction is an end-to-end Machine Learning project that predicts whether a telecom customer is likely to leave the company based on demographic and service usage information.

The project covers the complete ML lifecycle—from data preprocessing and model training to deployment using Streamlit, Docker containerization, and CI/CD automation with Jenkins.

---

# ✨ Features

- Customer Churn Prediction
- Data Cleaning & Feature Engineering
- Machine Learning Model
- Interactive Streamlit Web Application
- Docker Containerization
- Jenkins CI/CD Pipeline
- GitHub Version Control
- Automated Deployment

---

# 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Web Framework
- Streamlit

### DevOps & Cloud
- Docker
- Jenkins
- Git
- GitHub

---

# 📂 Project Structure

```text
Customer-Churn-Prediction
│
├── app/
├── data/
├── models/
├── notebooks/
├── screenshots/
├── src/
├── .streamlit/
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📸 Project Screenshots

## 🏠 Streamlit Home Page

![Home](screenshots/home.png)

---

## 📊 Customer Churn Prediction

![Prediction](screenshots/prediction.png)

---

## 🐳 Docker Container Running

![Docker](screenshots/docker-dashboard.png)

---

## ⚙️ Jenkins Build Success

![Jenkins](screenshots/jenkins-success.png)

---

## 🚀 Jenkins Pipeline

![Pipeline](screenshots/pipeline-overview.png)

---

# 🏗 System Architecture

```text
            Developer
                │
                ▼
            VS Code
                │
            git push
                │
                ▼
             GitHub
                │
                ▼
             Jenkins
                │
      ┌─────────┴─────────┐
      ▼                   ▼
 Install Dependencies   Build Docker Image
      │                   │
      └─────────┬─────────┘
                ▼
     Stop Existing Container
                │
                ▼
      Run Docker Container
                │
                ▼
      Streamlit Web Application
                │
                ▼
      Customer Churn Prediction
```

---

# 🤖 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- Docker Containerization
- Jenkins CI/CD Automation

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/sanjanahp16/Customer-Churn-Prediction.git
```

Move into the project

```bash
cd Customer-Churn-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

# 🐳 Docker

Build the image

```bash
docker build -t customer-churn-app .
```

Run the container

```bash
docker run -d -p 8501:8501 --name customer-churn customer-churn-app
```

Application URL

```text
http://localhost:8501
```

---

# ⚙️ Jenkins CI/CD Pipeline

Pipeline Stages

- ✅ Checkout Source Code
- ✅ Install Dependencies
- ✅ Build Docker Image
- ✅ Stop Existing Docker Container
- ✅ Run Docker Container

Every new commit pushed to GitHub can be automatically built and deployed using Jenkins.

---

# 📈 Future Improvements

- AWS EC2 Deployment
- Docker Hub Integration
- GitHub Actions
- Kubernetes Deployment
- Model Monitoring
- Automated Model Retraining
- User Authentication
- Database Integration

---

# 👩‍💻 Author

**Sanjana H P**

- GitHub: https://github.com/sanjanahp16
- LinkedIn: https://www.linkedin.com/in/sanjana-hp-66292b295/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.