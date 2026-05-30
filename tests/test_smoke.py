import pandas as pd
import os
import joblib
import pytest

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_path(filename):
    return os.path.join(BASE, "data", "processed", filename)

def test_cleaned_transactions_exists():
    df = pd.read_csv(get_path("cleaned_transactions.csv"))
    assert not df.empty
    assert "TotalPrice" in df.columns

def test_customer_segments_valid():
    df = pd.read_csv(get_path("customer_segments.csv"))
    assert "Segment" in df.columns
    assert len(df["Segment"].unique()) >= 3

def test_forecast_has_30_days():
    df = pd.read_csv(get_path("prophet_forecast_30d.csv"))
    assert len(df) >= 30
    assert "yhat" in df.columns

def test_churn_model_loads():
    model_path = os.path.join(BASE, "models", "xgb_churn_model.joblib")
    model = joblib.load(model_path)
    assert model is not None

def test_product_features_valid():
    df = pd.read_csv(get_path("product_features.csv"))
    assert "ProductRevenue" in df.columns
    assert df["ProductRevenue"].min() >= 0