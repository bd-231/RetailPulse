import streamlit as st

def setup_page(page_title, page_icon="📈"):
    st.set_page_config(
        page_title=f"{page_title} - RetailPulse",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Inject custom CSS for premium look
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"]  {
            font-family: 'Outfit', sans-serif !important;
        }
        
        .reportview-container {
            background-color: #f4f6f9;
        }
        .sidebar .sidebar-content {
            background-color: #e9ecef;
            color: #2c3e50;
        }
        /* Custom card styling */
        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            border: 1px solid #dee2e6;
        }
        .metric-title {
            font-size: 1.1rem;
            color: #7f8c8d;
            margin-bottom: 10px;
            font-weight: 600;
        }
        .metric-value {
            font-size: 2rem;
            color: #2c3e50;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)
    
def display_metric_card(title, value, prefix="", suffix=""):
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{prefix}{value}{suffix}</div>
        </div>
    """, unsafe_allow_html=True)
    
def display_header(title, subtitle=""):
    st.title(title)
    if subtitle:
        st.markdown(f"*{subtitle}*")
    st.markdown("---")
