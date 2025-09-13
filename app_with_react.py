import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime  # ADD THIS LINE
from truthlens_frontend import render_truthlens_app
from utils.ai_services import GeminiService
from utils.database import FirebaseService
from utils.news_services import NewsAggregator
from utils.security import SecurityService

# Configure Streamlit page
st.set_page_config(
    page_title="TruthLens - AI-Powered Misinformation Detection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar
)

# Hide all Streamlit UI elements to let React take over
hide_streamlit_style = """
<style>
    /* Hide Streamlit's default elements */
    .main > div { padding-top: 0px !important; padding-bottom: 0px !important; }
    header[data-testid="stHeader"] { display: none !important; }
    div[data-testid="stSidebar"] { display: none !important; }
    footer { display: none !important; }
    .stApp > header { display: none !important; }
    .stApp { margin: 0 !important; padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* Ensure full width and height */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Initialize your existing backend services
@st.cache_resource
def initialize_services():
    """Initialize all backend services"""
    return {
        'ai': GeminiService(),
        'database': FirebaseService(),
        'news': NewsAggregator(),
        'security': SecurityService()
    }

# Get services
services = initialize_services()

# Check services status for React frontend
services_status = {
    'ai': True,  # You can add actual health checks here
    'database': True,
    'news': True,
    'security': True
}

# Render your complete React frontend directly (no loading text)

# This renders your entire React app and handles communication
component_value = render_truthlens_app(
    key="truthlens_main",
    services_status=services_status,
    user_data={},
    width=1200,
    height=1000
)

# Handle communication from React frontend
if component_value:
    action = component_value.get('action')
    
    if action == 'analyze_text':
        text_to_analyze = component_value.get('text', '')
        
        # Show analysis in progress
        with st.spinner('🔍 Analyzing content...'):
            # Use your existing forensic analysis
            analysis_result = services['ai'].forensic_analysis(text_to_analyze)
            
            # Extract sources and reporting info
            sources_info = services['ai'].extract_sources_and_reporting(analysis_result)
            
                        # Store in database (match the expected format)
            mock_results = {
                'risk_score': 75,  # You can extract this from analysis_result later
                'credibility_score': 25,
                'manipulation_tactics': ['AI Analysis']
            }
            services['database'].save_analysis(text_to_analyze, mock_results)

        
        # Display results
        if analysis_result:
            st.success("✅ Analysis Complete!")
            st.markdown("### 📋 Forensic Analysis Results")
            st.markdown(analysis_result)
            
            # Show sources if available
            if sources_info.get('sources'):
                st.markdown("### 🔗 Verification Sources")
                for source in sources_info['sources']:
                    st.markdown(f"- **{source['name']}**: {source['description']}")
       
    elif action == 'analyze_image':
        # Handle image analysis
        image_data = component_value.get('image_data')
        # Your existing image analysis logic here
        pass
        
    elif action == 'get_news':
        # Handle news requests
        news_data = services['news'].get_breaking_news()
        # Send back to React
        pass
        
    elif action == 'authority_login':
        # Handle authority authentication
        credentials = component_value.get('credentials')
        auth_result = services['security'].verify_authority_credentials(credentials)
        # Handle authentication result
        pass

    # Add more action handlers as needed for your 5 page types:
    # Home, Archive, Learn, Authority, Language switching

# Display connection status
with st.expander("🔧 Backend Services Status", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AI Service", "🟢 Connected" if services_status['ai'] else "🔴 Disconnected")
    with col2:
        st.metric("Database", "🟢 Connected" if services_status['database'] else "🔴 Disconnected")
    with col3:
        st.metric("News Service", "🟢 Connected" if services_status['news'] else "🔴 Disconnected")
    with col4:
        st.metric("Security", "🟢 Connected" if services_status['security'] else "🔴 Disconnected")

