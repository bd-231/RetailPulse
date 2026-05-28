import streamlit as st
import plotly.express as px
from utils.ui import setup_page, display_header
from utils.data_loader import get_processed_data

setup_page("Churn Analysis")
display_header("Churn Analysis", "Customer Attrition Metrics")

with st.spinner("Loading churn data..."):
    df_customers = get_processed_data('customer_features.csv')

if not df_customers.empty and 'CustomerActivityStatus' in df_customers.columns:
    st.subheader("Churn Statistics")
    
    churn_counts = df_customers['CustomerActivityStatus'].value_counts()
    churn_rate = (churn_counts.get('Churned', 0) / len(df_customers)) * 100
    
    col1, col2 = st.columns(2)
    col1.metric("Overall Churn Rate", f"{churn_rate:.1f}%")
    col2.metric("Total Churned Customers", f"{churn_counts.get('Churned', 0):,}")
    
    col3, col4 = st.columns(2)
    
    with col3:
        fig_pie = px.pie(names=churn_counts.index, values=churn_counts.values, 
                         title="Customer Status Distribution", hole=0.3,
                         color=churn_counts.index,
                         color_discrete_map={"Active": "#2ecc71", "Churned": "#e74c3c"})
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col4:
        # Compare Average Order Size between active and churned
        if 'AverageBasketSize' in df_customers.columns:
            fig_box = px.box(df_customers, x='CustomerActivityStatus', y='AverageBasketSize',
                             title="Avg Basket Size: Active vs Churned",
                             color='CustomerActivityStatus',
                             color_discrete_map={"Active": "#2ecc71", "Churned": "#e74c3c"},
                             template="plotly_white")
            # Limit y axis to remove extreme outliers visually if needed, but Plotly handles it well
            st.plotly_chart(fig_box, use_container_width=True)
            
    st.subheader("At-Risk / Churned Customers Directory")
    # Show customers who are churned or have high gap
    at_risk = df_customers[df_customers['CustomerActivityStatus'] == 'Churned']
    st.dataframe(at_risk.sort_values(by='TotalRevenue', ascending=False).head(100), use_container_width=True)
    
    st.markdown("---")
    st.subheader("Export Data")
    csv = at_risk.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download At-Risk Customers List",
        data=csv,
        file_name='at_risk_customers.csv',
        mime='text/csv',
    )
else:
    st.warning("Churn data not found or missing required columns.")
