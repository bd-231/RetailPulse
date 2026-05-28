import streamlit as st
import plotly.graph_objects as go
from utils.ui import setup_page, display_header
from utils.data_loader import get_processed_data

setup_page("Demand Forecasting")
display_header("Demand Forecasting", "30-Day Sales Predictions")

with st.spinner("Loading forecast data..."):
    df_forecast = get_processed_data('prophet_forecast_30d.csv')

if not df_forecast.empty:
    st.subheader("30-Day Sales Forecast")
    
    # Calculate key metrics
    total_forecast_revenue = df_forecast['yhat'].sum()
    avg_daily_forecast = df_forecast['yhat'].mean()
    
    col1, col2 = st.columns(2)
    col1.metric("Predicted 30-Day Revenue", f"£{total_forecast_revenue:,.0f}")
    col2.metric("Average Daily Predicted", f"£{avg_daily_forecast:,.0f}")
    
    # Forecast trend graph with confidence intervals
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        name='Upper Bound',
        x=df_forecast['ds'],
        y=df_forecast['yhat_upper'],
        mode='lines',
        marker=dict(color="#bdc3c7"),
        line=dict(width=0),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        name='Lower Bound',
        x=df_forecast['ds'],
        y=df_forecast['yhat_lower'],
        mode='lines',
        marker=dict(color="#bdc3c7"),
        line=dict(width=0),
        fillcolor='rgba(189, 195, 199, 0.3)',
        fill='tonexty',
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        name='Forecast (yhat)',
        x=df_forecast['ds'],
        y=df_forecast['yhat'],
        mode='lines+markers',
        line=dict(color="#e67e22")
    ))
    
    fig.update_layout(title="Forecast Trend with Confidence Intervals", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Export Data")
    csv = df_forecast.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Forecast Data",
        data=csv,
        file_name='demand_forecast_30d.csv',
        mime='text/csv',
    )
else:
    st.warning("Forecast data not found.")
