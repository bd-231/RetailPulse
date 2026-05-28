import streamlit as st
import plotly.express as px
from utils.ui import setup_page, display_header
from utils.data_loader import get_processed_data

setup_page("Inventory Optimization")
display_header("Inventory Optimization", "Product Performance and Reorder Alerts")

with st.spinner("Loading inventory data..."):
    df_products = get_processed_data('product_features.csv')

if not df_products.empty:
    st.subheader("Product Performance Overview")
    
    # Define fast vs slow moving based on frequency median
    median_freq = df_products['ProductDemandFrequency'].median()
    df_products['Velocity'] = df_products['ProductDemandFrequency'].apply(lambda x: 'Fast-Moving' if x >= median_freq else 'Slow-Moving')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Fast-Moving Products")
        fast_moving = df_products[df_products['Velocity'] == 'Fast-Moving'].sort_values('ProductRevenue', ascending=False)
        st.dataframe(fast_moving[['StockCode', 'Description', 'ProductRevenue', 'ProductDemandFrequency']].head(50), use_container_width=True)
        
    with col2:
        st.write("### Slow-Moving Products")
        slow_moving = df_products[df_products['Velocity'] == 'Slow-Moving'].sort_values('ProductRevenue', ascending=True)
        st.dataframe(slow_moving[['StockCode', 'Description', 'ProductRevenue', 'ProductDemandFrequency']].head(50), use_container_width=True)
        
    st.markdown("---")
    st.subheader("Revenue vs Demand Frequency")
    
    fig = px.scatter(df_products, x='ProductDemandFrequency', y='ProductRevenue', 
                     color='Velocity', hover_data=['Description', 'StockCode'],
                     title="Product Velocity and Revenue",
                     color_discrete_map={"Fast-Moving": "#2ecc71", "Slow-Moving": "#e74c3c"},
                     template="plotly_white")
    
    # Log scale is often better for this kind of distribution
    fig.update_xaxes(type="log", title="Demand Frequency (Log Scale)")
    fig.update_yaxes(type="log", title="Revenue (Log Scale)")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Export Recommendations")
    csv = df_products.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Full Inventory Analysis",
        data=csv,
        file_name='inventory_analysis.csv',
        mime='text/csv',
    )
else:
    st.warning("Product features data not found.")
