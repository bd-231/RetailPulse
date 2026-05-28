import streamlit as st
import plotly.express as px
from utils.ui import setup_page, display_header
from utils.data_loader import get_processed_data

setup_page("Customer Segmentation")
display_header("Customer Segmentation", "RFM Analysis and Customer Clusters")

with st.spinner("Loading customer segments..."):
    df_segments = get_processed_data('customer_segments.csv')

if not df_segments.empty:
    st.subheader("Segment Distribution")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        segment_counts = df_segments['Segment'].value_counts().reset_index()
        segment_counts.columns = ['Segment', 'Count']
        fig_pie = px.pie(segment_counts, names='Segment', values='Count', title="Customers by Segment", hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        # Display VIP/Loyal/At-Risk customers (first 100 to avoid freezing)
        st.write("### Customer Directory")
        st.dataframe(df_segments[['CustomerID', 'Segment', 'Recency', 'Frequency', 'Monetary']].head(100), use_container_width=True)

    st.markdown("---")
    st.subheader("RFM Visualizations")
    
    tab1, tab2 = st.tabs(["Recency vs Monetary", "Frequency vs Monetary"])
    
    with tab1:
        fig_scatter1 = px.scatter(df_segments, x='Recency', y='Monetary', color='Segment', 
                                 title="Recency vs Monetary Value",
                                 hover_data=['CustomerID'],
                                 template="plotly_white")
        st.plotly_chart(fig_scatter1, use_container_width=True)
        
    with tab2:
        fig_scatter2 = px.scatter(df_segments, x='Frequency', y='Monetary', color='Segment', 
                                 title="Frequency vs Monetary Value",
                                 hover_data=['CustomerID'],
                                 template="plotly_white")
        st.plotly_chart(fig_scatter2, use_container_width=True)
        
    st.markdown("---")
    st.subheader("Export Data")
    csv = df_segments.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Customer Segmentation Report",
        data=csv,
        file_name='customer_segmentation_report.csv',
        mime='text/csv',
    )
else:
    st.warning("Customer segmentation data not found.")
