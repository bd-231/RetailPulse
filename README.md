# 📊 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

> Predictive Demand • Customer Segmentation • Churn Analysis • Inventory Optimization

🚀 **Live Demo**: https://retailpulse-zidio123.streamlit.app

---

## 📌 Project Overview

RetailPulse is an end-to-end data science platform built for retail businesses to make smarter, data-driven decisions. It ingests historical sales transaction data and delivers four core outputs — demand forecasts, customer segments, churn risk predictions, and inventory reorder recommendations — all accessible through an interactive dashboard.

**Business Impact Targets:**
- Reduce stockouts by **30–50%** through accurate demand forecasting
- Increase revenue by **15–25%** through better inventory decisions
- Improve customer retention by identifying at-risk customers early
- Handle **10M+ transactions** per month with batch jobs under 5 minutes

---

## 👥 Team

| Name | Responsibility |
|------|---------------|
| Bhagyesh Patil | Demand forecasting, inventory optimization |
| Komal Nitesh Agrawal | Customer segmentation, churn prediction |
| Mann Savsani | Data ingestion, cleaning, EDA  |
| Priyanshu Mukherjee | Deployment, containerization, CI/CD, MLOps |

---

## ✨ Features

| ID | Feature | Description | Success Metric |
|----|---------|-------------|----------------|
| F01 | Data Ingestion & Cleaning | Automated ETL pipeline with data quality checks | Clean dataset, no nulls |
| F02 | Customer Segmentation | RFM scoring + K-Means clustering | 6–8 meaningful segments |
| F03 | Demand Forecasting | Prophet time-series, 30-day predictions | MAPE ≤ 12% |
| F04 | Churn Prediction | XGBoost classifier on behavioral features | AUC-ROC ≥ 0.88 |
| F05 | Inventory Optimization | Reorder logic based on forecasted demand | Reduce overstock by 25–40% |
| F06 | Analytics Dashboard | Interactive Streamlit multi-page app | Real-time insights |

---

## 🛠️ Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Language | Python 3.11 | Data science ecosystem |
| Dashboard | Streamlit | Pure Python, no HTML needed |
| Forecasting | Prophet | Handles seasonality automatically |
| Churn Model | XGBoost | Best performance on tabular data |
| Segmentation | K-Means | Fast, scalable clustering |
| Experiment Tracking | MLflow | Open source, reproducible runs |
| Drift Detection | Evidently AI | Catches model staleness early |
| Containerization | Docker | Consistent cross-environment deployment |
| Orchestration | Kubernetes | Auto-scaling in production |
| CI/CD | GitHub Actions | Automated testing on every push |
| Deployment | Streamlit Community Cloud | Free, instant, HTTPS |

---

## 📁 Project Structure

```
RetailPulse/
├── .github/
│   └── workflows/
│       └── ci.yml                    # CI/CD pipeline
├── data/
│   ├── processed/                    # Feature-engineered CSVs
│   └── raw/                          # Original transaction data
├── k8s/
│   └── deployment.yaml               # Kubernetes manifests
├── models/
│   ├── xgb_churn_model.joblib
│   ├── customer_segmentation_model.pkl
│   └── demand_forecasting_model.json
├── notebooks/
│   ├── week_1.ipynb                  # EDA and data cleaning
│   ├── week_2.ipynb                  # ML modeling
│   └── week_3_mlops.ipynb            # MLflow + drift detection
├── pages/
│   ├── 1_Sales_Analytics.py
│   ├── 2_Customer_Segmentation.py
│   ├── 3_Demand_Forecasting.py
│   ├── 4_Churn_Analysis.py
│   └── 5_Inventory_Optimization.py
├── reports/
│   └── data_drift_report.html
├── tests/
│   └── test_smoke.py                 # 5 automated smoke tests
├── utils/
│   ├── data_loader.py
│   └── ui.py
├── app.py                            # Main Streamlit entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/bd-231/RetailPulse.git
cd RetailPulse

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

App opens at **http://localhost:8501**

---

## 🐳 Docker

```bash
# Build image
docker build -t retailpulse .

# Run container
docker run -p 8501:8501 retailpulse
```

---

## 🧪 Tests

```bash
python -m pytest tests/ -v
```

5 smoke tests validate data pipelines, model loading, and forecast integrity.

---

## 📊 Model Performance

| Model | Metric | Target | Achieved |
|-------|--------|--------|----------|
| Prophet Forecasting | MAPE | ≤ 12% | ✅ |
| XGBoost Churn | AUC-ROC | ≥ 0.88 | ✅ 0.91 |
| K-Means Segmentation | Segments | 6–8 | ✅ 6 segments |

---

## ⚙️ MLOps

- **MLflow** — tracks every model training run with parameters, metrics, and artifacts logged
- **Evidently AI** — generates data drift reports comparing reference vs current customer data
- **GitHub Actions** — CI pipeline runs on every push: install → test → docker build
- **Kubernetes HPA** — auto-scales containers when CPU exceeds 70%

---

*Built under Zidio Development — Data Science & Analytics Domain • March 2026*