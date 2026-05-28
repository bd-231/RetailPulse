import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"Data file not found: {file_path}")
        return pd.DataFrame()
    
    # Try parsing dates based on common date columns in this project
    df = pd.read_csv(file_path)
    
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    if 'InvoiceDate' in df.columns:
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    if 'ds' in df.columns:
        df['ds'] = pd.to_datetime(df['ds'])
        
    return df

@st.cache_data
def get_processed_data(filename):
    # Calculate relative path based on data_loader.py location (utils/ -> ../data/processed/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'processed', filename)
    return load_data(file_path)

def load_all_core_data():
    """Loads all commonly used datasets for the dashboard"""
    return {
        'transactions': get_processed_data('cleaned_transactions.csv'),
        'daily_sales': get_processed_data('daily_sales.csv'),
        'customer_segments': get_processed_data('customer_segments.csv'),
        'customer_features': get_processed_data('customer_features.csv'),
        'product_features': get_processed_data('product_features.csv'),
        'forecast': get_processed_data('prophet_forecast_30d.csv')
    }
