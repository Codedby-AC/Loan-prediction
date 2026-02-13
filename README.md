# Loan Approval Prediction System

## 📌 Overview

This project is a full-stack Machine Learning application that predicts
loan approval status using a Neural Network model built with PyTorch.

## 🚀 Features

-   Real-time loan approval prediction
-   Probability score output
-   REST API using FastAPI
-   Interactive frontend using Streamlit
-   Docker-ready deployment
-   Scalable production setup with Gunicorn

## 🛠 Technologies Used

-   Python
-   PyTorch
-   Scikit-learn
-   FastAPI
-   Streamlit
-   Docker
-   Nginx

## ⚙ Installation & Setup

### 1. Clone Repository

``` bash
git clone <your-repo-url>
cd loan_prediction
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3. Run Backend

``` bash
uvicorn backend:app --reload
```

### 4. Run Frontend

``` bash
streamlit run frontend.py
```

## 🐳 Docker Deployment

``` bash
docker build -t loan_app .
docker run -p 8000:8000 loan_app
```

## 🌐 Production Deployment

Use Gunicorn + Uvicorn workers behind Nginx reverse proxy.

## 📈 Future Improvements

-   Use XGBoost for better accuracy
-   Add database integration
-   Add authentication system
-   Deploy on AWS / GCP with auto scaling

## 👨‍💻 Author

Loan Prediction ML Project

