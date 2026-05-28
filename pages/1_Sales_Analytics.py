import streamlit as st
import pandas as pd
import plotly.express as px
from utils.ui import setup_page, display_header
from utils.data_loader import get_processed_data

setup_page("Sales Analytics")
display_header("Sales Analytics", "Revenue Trends and Distribution")

with st.spinner("Loading sales data..."):
    df_daily = get_processed_data('daily_sales.csv')
    df_trans = get_processed_data('cleaned_transactions.csv')

if not df_trans.empty and not df_daily.empty:
    st.sidebar.header("Filters")
    
    # Country Filter
    countries = ["All"] + list(df_trans['Country'].dropna().unique())
    selected_country = st.sidebar.selectbox("Select Country", countries)
    
    # Date Range Filter
    min_date = df_trans['InvoiceDate'].min().date()
    max_date = df_trans['InvoiceDate'].max().date()
    start_date, end_date = st.sidebar.date_input("Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
    
    # Apply Filters
    mask = (df_trans['InvoiceDate'].dt.date >= start_date) & (df_trans['InvoiceDate'].dt.date <= end_date)
    if selected_country != "All":
        mask = mask & (df_trans['Country'] == selected_country)
        
    filtered_trans = df_trans[mask]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Daily Sales Trend")
        # For simplicity, we just aggregate the filtered data
        daily_agg = filtered_trans.groupby(filtered_trans['InvoiceDate'].dt.date)['TotalPrice'].sum().reset_index()
        daily_agg.columns = ['Date', 'Revenue']
        if not daily_agg.empty:
            fig_daily = px.line(daily_agg, x='Date', y='Revenue', title="Daily Revenue", template="plotly_white")
            fig_daily.update_traces(line_color="#2c3e50")
            st.plotly_chart(fig_daily, use_container_width=True)
        else:
            st.info("No data available for the selected filters.")
            
    with col2:
        st.subheader("Revenue by Country (Top 10)")
        country_rev = filtered_trans.groupby('Country')['TotalPrice'].sum().nlargest(10).reset_index()
        if not country_rev.empty:
            fig_country = px.bar(country_rev, x='Country', y='TotalPrice', title="Top 10 Countries by Revenue", template="plotly_white")
            fig_country.update_traces(marker_color="#3498db")
            st.plotly_chart(fig_country, use_container_width=True)
        
    st.subheader("Monthly Sales Trend")
    filtered_trans['Month_Year'] = filtered_trans['InvoiceDate'].dt.to_period('M').astype(str)
    monthly_agg = filtered_trans.groupby('Month_Year')['TotalPrice'].sum().reset_index()
    if not monthly_agg.empty:
        fig_monthly = px.bar(monthly_agg, x='Month_Year', y='TotalPrice', title="Monthly Revenue", template="plotly_white")
        fig_monthly.update_traces(marker_color="#e74c3c")
        st.plotly_chart(fig_monthly, use_container_width=True)
        
    st.markdown("---")
    st.subheader("Export Data")
    csv = filtered_trans.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Sales Data as CSV",
        data=csv,
        file_name='filtered_sales_data.csv',
        mime='text/csv',
    )
else:
    st.warning("Data not found.")
