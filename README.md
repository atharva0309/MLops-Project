# 🚗 Vehicle Insurance Prediction – End-to-End MLOps Project  

An end-to-end **MLOps pipeline** for predicting the likelihood of a customer purchasing vehicle insurance.  
This project demonstrates modular workflows for **data ingestion, preprocessing, training, evaluation, deployment, and monitoring** using modern MLOps practices.  

---

## 📌 Project Overview
Insurance companies need accurate predictions to improve customer targeting and policy conversions.  
This project builds a complete ML system that:  
- Ingests raw data from multiple sources  
- Validates and transforms it for model training  
- Trains a predictive ML model  
- Automates CI/CD with containerization and cloud deployment  
- Exposes predictions via a **FastAPI REST API**  

---

## ⚡ Features
- **Data Pipeline** – ingestion, validation, transformation, and feature engineering  
- **Model Pipeline** – training, evaluation, and experiment tracking  
- **CI/CD Automation** – GitHub Actions for testing & deployment  
- **Containerization** – Dockerized services for reproducibility  
- **Cloud Deployment** – hosted on AWS (EC2, S3, ECR)  
- **API Service** – FastAPI endpoint for real-time inference  

---

## 🛠️ Tech Stack
- **Language**: Python 3  
- **Frameworks**: Scikit-learn, FastAPI, PyTorch (optional extensions)  
- **MLOps Tools**: Docker, GitHub Actions, AWS (EC2, S3, ECR)  
- **Others**: Pandas, NumPy, Matplotlib, Logging  

---

## 🏗️ System Architecture
```mermaid
flowchart TD
    A[Raw Data] --> B[Data Ingestion]
    B --> C[Data Validation & Transformation]
    C --> D[Model Training]
    D --> E[Evaluation]
    E --> F[Docker + CI/CD Pipeline]
    F --> G[AWS Deployment]
    G --> H[FastAPI Prediction Service]
