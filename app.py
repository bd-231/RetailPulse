import streamlit as st
import pandas as pd
from utils.ui import setup_page, display_metric_card, display_header
from utils.data_loader import load_all_core_data

# Set up page configuration
setup_page("Home")

display_header("RetailPulse Executive Dashboard", "Comprehensive Overview of E-commerce Performance")

# Show loading spinner while fetching data
with st.spinner("Loading core datasets..."):
    data = load_all_core_data()
    df_trans = data.get('transactions', pd.DataFrame())
    df_customers = data.get('customer_features', pd.DataFrame())

if not df_trans.empty and not df_customers.empty:
    st.subheader("Global KPIs")
    
    # Calculate KPIs
    total_revenue = df_trans['TotalPrice'].sum()
    total_orders = df_trans['Invoice'].nunique()
    total_customers = df_customers['Customer ID'].nunique()
    # Handle both Active/Churned text mapping or raw stats
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric_card("Total Revenue", f"{total_revenue:,.0f}", prefix="£")
    with col2:
        display_metric_card("Total Orders", f"{total_orders:,}")
    with col3:
        display_metric_card("Total Customers", f"{total_customers:,}")
    with col4:
        display_metric_card("Avg Order Value", f"{avg_order_value:,.2f}", prefix="£")
        
    st.markdown("---")
    
    st.subheader("Welcome to RetailPulse")
    st.markdown("""
    This dashboard provides a suite of analytics tools designed to give you deep insights into your retail performance. 
    Use the sidebar to navigate through the different analytical modules:
    
    - **Sales Analytics**: Track daily and monthly revenue trends.
    - **Customer Segmentation**: Understand your customer base through RFM analysis.
    - **Demand Forecasting**: Plan ahead with 30-day AI-powered sales predictions.
    - **Churn Analysis**: Identify and prevent customer attrition.
    - **Inventory Optimization**: Manage your fast and slow-moving products effectively.
    """)
    
    # Optionally, we can show a quick snapshot chart here
    st.info("👈 Please select a dashboard from the sidebar to begin.")
else:
    st.warning("Data not found. Please ensure the data pipelines have been run and data exists in data/processed/")
