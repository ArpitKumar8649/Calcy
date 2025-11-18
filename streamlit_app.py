"""
TalentScout AI Hiring Assistant - Main Streamlit Application
Phase 1: Basic Setup with Placeholder UI
"""
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
import os
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables
load_dotenv('.env.streamlit')

from config.settings import settings
from utils.constants import ConversationStage, REQUIRED_FIELDS
from utils.helpers import is_exit_keyword

# Page configuration
st.set_page_config(
    page_title=settings.app_title,
    page_icon=settings.app_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Subheader styling */
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin: 0.5rem 0;
        animation: fadeIn 0.3s ease-in;
    }
    
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    
    /* Sidebar styling */
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .info-card {
        background: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    .info-label {
        font-weight: 600;
        color: #555;
        font-size: 0.9rem;
    }
    
    .info-value {
        color: #333;
        font-size: 1rem;
        margin-top: 0.3rem;
    }
    
    /* Progress bar styling */
    .progress-container {
        background: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        margin: 1rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    /* Status badge */
    .status-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    .badge-pending {
        background-color: #fff3e0;
        color: #f57c00;
    }
    
    .badge-collected {
        background-color: #e8f5e9;
        color: #2e7d32;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Info box */
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'candidate_data' not in st.session_state:
        st.session_state.candidate_data = {
            'full_name': None,
            'email': None,
            'phone': None,
            'years_experience': None,
            'desired_positions': None,
            'current_location': None,
            'tech_stack': None
        }
    
    if 'conversation_stage' not in st.session_state:
        st.session_state.conversation_stage = ConversationStage.GREETING.value
    
    if 'letta_connected' not in st.session_state:
        st.session_state.letta_connected = False
    
    if 'conversation_started' not in st.session_state:
        st.session_state.conversation_started = False


def render_sidebar():
    """Render sidebar with candidate summary"""
    with st.sidebar:
        st.markdown('<p class="sidebar-header">📋 Candidate Summary</p>', unsafe_allow_html=True)
        
        # Progress indicator
        collected_fields = sum(1 for v in st.session_state.candidate_data.values() if v is not None)
        total_fields = len(REQUIRED_FIELDS)
        progress_percentage = (collected_fields / total_fields) * 100
        
        st.markdown(f"""
        <div style="margin: 1rem 0;">
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">
                Information Collected: {collected_fields}/{total_fields}
            </p>
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress_percentage}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display collected information
        st.markdown("---")
        
        if collected_fields == 0:
            st.info("💬 Start the conversation to collect candidate information.")
        else:
            for field, value in st.session_state.candidate_data.items():
                field_name = field.replace('_', ' ').title()
                if value:
                    st.markdown(f"""
                    <div class="info-card">
                        <p class="info-label">{field_name}</p>
                        <p class="info-value">{value}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <span class="status-badge badge-pending">{field_name}: Pending</span>
                    """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # About section
        st.subheader("ℹ️ About")
        st.markdown("""
        This AI assistant helps with initial candidate screening by:
        - 📝 Gathering essential information
        - 💻 Assessing technical skills  
        - 🎯 Generating relevant questions
        - 🤝 Maintaining professional conversation
        """)
        
        st.markdown("---")
        
        # Status section
        st.subheader("⚙️ Status")
        if st.session_state.letta_connected:
            st.success("✅ Letta Agent Connected")
        else:
            st.warning("⚠️ Letta Integration Pending")
            st.info("Phase 2 will integrate Letta agent")
        
        # Reset button
        if st.button("🔄 Reset Conversation", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


def render_welcome_message():
    """Render welcome message for new conversations"""
    st.markdown("""
    <div class="info-box">
        <h3>👋 Welcome to TalentScout AI Hiring Assistant!</h3>
        <p>I'm here to help with your initial candidate screening. I'll:</p>
        <ul>
            <li>Collect your basic information</li>
            <li>Understand your technical expertise</li>
            <li>Ask relevant technical questions</li>
            <li>Provide a smooth interview experience</li>
        </ul>
        <p><strong>Ready to begin? Type 'hello' or 'start' to get started!</strong></p>
    </div>
    """, unsafe_allow_html=True)


def render_phase_warning():
    """Render warning about Phase 1 limitations"""
    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ Phase 1: Development Mode</h4>
        <p>Currently showing placeholder functionality. Features coming in next phases:</p>
        <ul>
            <li><strong>Phase 2:</strong> Letta Agent Integration</li>
            <li><strong>Phase 3:</strong> Conversation Flow Logic</li>
            <li><strong>Phase 4:</strong> Technical Question Generation</li>
        </ul>
        <p><em>The chatbot will provide intelligent responses once Letta credentials are configured.</em></p>
    </div>
    """, unsafe_allow_html=True)


def handle_user_input(user_input: str):
    """Handle user input and generate responses (Phase 1 placeholder)"""
    
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Check for exit keywords
    if is_exit_keyword(user_input):
        response = """
        Thank you for your time! Your information has been recorded. 
        Our team will review your profile and get back to you soon.
        
        Have a great day! 👋
        """
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        return
    
    # Placeholder responses for Phase 1
    if not st.session_state.conversation_started:
        response = """
        Great! Let's get started with your screening interview.
        
        First, could you please tell me your full name?
        """
        st.session_state.conversation_started = True
    else:
        # Generate contextual placeholder responses
        message_count = len([m for m in st.session_state.messages if m['role'] == 'user'])
        
        if message_count == 2:
            response = "Thank you! Now, what's your email address?"
        elif message_count == 3:
            response = "Perfect! Could you share your phone number?"
        elif message_count == 4:
            response = "Got it! How many years of experience do you have?"
        elif message_count == 5:
            response = "Excellent! What position(s) are you interested in?"
        elif message_count == 6:
            response = "Great! Where are you currently located?"
        elif message_count == 7:
            response = """
            Perfect! Now, let's talk about your technical skills.
            
            Could you please list your tech stack? Include:
            - Programming languages (e.g., Python, JavaScript)
            - Frameworks (e.g., React, Django)
            - Databases (e.g., MongoDB, PostgreSQL)
            - Tools (e.g., Docker, AWS)
            """
        else:
            response = """
            🔧 **Phase 1 Placeholder Response**
            
            In Phase 2, the Letta agent will:
            - Understand your responses contextually
            - Update memory blocks automatically  
            - Generate relevant technical questions
            - Maintain natural conversation flow
            
            For now, I'm collecting your input and demonstrating the UI!
            Type 'bye' to end the conversation.
            """
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


def main():
    """Main application entry point"""
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown(
        f'<h1 class="main-header">{settings.app_icon} {settings.app_title}</h1>', 
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub-header">Powered by Letta Agent Framework 🤖</p>',
        unsafe_allow_html=True
    )
    st.markdown('---')
    
    # Render sidebar
    render_sidebar()
    
    # Main chat interface
    st.subheader("💬 Chat Interface")
    
    # Show phase warning
    render_phase_warning()
    
    # Display chat messages
    chat_container = st.container()
    with chat_container:
        if len(st.session_state.messages) == 0:
            render_welcome_message()
        else:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here...", key="user_input"):
        # Display user message immediately
        with st.chat_message("user"):
            st.write(prompt)
        
        # Process and respond
        handle_user_input(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(st.session_state.messages[-1]["content"])
        
        # Rerun to update UI
        st.rerun()


if __name__ == "__main__":
    main()
