# 🤖 AI HIRING ASSISTANT CHATBOT - IMPLEMENTATION PLAN
## Using Streamlit + Letta Agent Framework

---

## 📚 TABLE OF CONTENTS
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Letta Agent Architecture](#letta-agent-architecture)
4. [Phase-by-Phase Implementation](#phase-by-phase-implementation)
5. [Project Structure](#project-structure)
6. [Environment Setup](#environment-setup)
7. [Testing Strategy](#testing-strategy)
8. [Deployment Plan](#deployment-plan)

---

## 🎯 PROJECT OVERVIEW

**Project Name:** TalentScout AI Hiring Assistant  
**Framework:** Streamlit (Python-based UI)  
**AI Engine:** Letta Agent (Stateful LLM Agent with Memory)  
**Purpose:** Automated candidate screening and technical assessment

### Key Features
- ✅ Intelligent conversation flow with context awareness
- ✅ Dynamic candidate information gathering
- ✅ Tech stack-specific question generation
- ✅ Persistent memory across conversation
- ✅ Graceful error handling and fallback mechanisms
- ✅ GDPR-compliant data handling

---

## 🛠️ TECHNOLOGY STACK

### Core Technologies
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **UI Framework** | Streamlit | 1.32.0+ | Chat interface & user interaction |
| **AI Agent** | Letta Agent | Latest | Stateful conversation management |
| **Language** | Python | 3.10+ | Backend logic |
| **Data Storage** | MongoDB / JSON | - | Candidate data persistence |
| **SDK** | letta-client | Latest | Letta API integration |

### Why Letta Agent?
- **Stateful Memory:** Maintains context across entire conversation
- **Memory Blocks:** Separate blocks for persona, user info, conversation state
- **Autonomous Memory Management:** Agent updates memory automatically
- **Tool Support:** Can extend with custom functions
- **Streaming Support:** Real-time response generation

---

## 🧠 LETTA AGENT ARCHITECTURE

### Memory Block Design

Our Letta agent will use the following memory blocks:

#### 1. **Persona Block** (Agent Identity)
```
Label: "persona"
Content: 
  - Name: TalentScout AI Assistant
  - Role: Initial candidate screening interviewer
  - Personality: Professional, friendly, encouraging
  - Guidelines: Stay focused on gathering information and technical assessment
```

#### 2. **Human Block** (Candidate Information)
```
Label: "human"
Content: {
  - full_name: ""
  - email: ""
  - phone: ""
  - years_experience: ""
  - desired_positions: []
  - current_location: ""
  - tech_stack: {
      languages: [],
      frameworks: [],
      databases: [],
      tools: []
    }
  - technical_answers: []
}
```

#### 3. **Conversation State Block** (Flow Management)
```
Label: "conversation_state"
Content: {
  - current_stage: "greeting" | "info_collection" | "tech_questions" | "conclusion"
  - info_collected: {
      name: false,
      email: false,
      phone: false,
      experience: false,
      position: false,
      location: false,
      tech_stack: false
    }
  - questions_asked: 0
  - questions_generated: []
}
```

#### 4. **Guidelines Block** (Agent Instructions)
```
Label: "guidelines"
Content:
  - Never deviate from hiring assistant purpose
  - Validate email format
  - Ensure tech stack is clearly understood
  - Generate 3-5 questions per tech stack
  - Be conversational but professional
  - Handle unclear inputs gracefully
```

### Letta Agent Capabilities

**Built-in Memory Tools:**
- `memory_replace`: Update specific fields (e.g., candidate name)
- `memory_insert`: Add new information to blocks
- `memory_rethink`: Restructure entire memory blocks

**Custom Tools (We'll Create):**
- `validate_email`: Check email format validity
- `generate_technical_questions`: Create tech-specific questions
- `save_candidate_data`: Persist data to database
- `check_conversation_end`: Detect exit keywords

---

## 📋 PHASE-BY-PHASE IMPLEMENTATION

---

### **PHASE 1: PROJECT SETUP & FOUNDATION** 
**Duration:** 2-3 hours  
**Status:** 🟡 READY TO START

#### Objectives
- Set up Streamlit application structure
- Install required dependencies
- Configure environment variables
- Create placeholder for Letta integration

#### Tasks

##### 1.1 Create Project Structure
```
/app/
├── streamlit_app.py              # Main Streamlit application
├── streamlit_requirements.txt     # Dependencies
├── .env.streamlit                 # Environment variables (Letta credentials)
├── config/
│   ├── __init__.py
│   ├── settings.py                # Configuration management
│   └── letta_config.py           # Letta-specific configurations
├── components/
│   ├── __init__.py
│   ├── chat_interface.py         # Chat UI components
│   ├── sidebar.py                # Sidebar with candidate summary
│   └── conversation_display.py   # Message display logic
├── services/
│   ├── __init__.py
│   ├── letta_service.py          # Letta agent interaction layer
│   ├── data_service.py           # Data persistence logic
│   └── validation_service.py     # Input validation
├── utils/
│   ├── __init__.py
│   ├── helpers.py                # Utility functions
│   └── constants.py              # Constants and enums
├── data/
│   └── candidates/               # Candidate data storage (JSON)
├── tests/
│   ├── __init__.py
│   ├── test_letta_service.py
│   └── test_validation.py
├── docs/
│   └── README.md                 # Comprehensive documentation
└── .gitignore
```

##### 1.2 Install Dependencies
Create `streamlit_requirements.txt`:
```txt
streamlit==1.32.0
letta-client==0.7.0
python-dotenv==1.0.1
pydantic==2.6.4
pymongo==4.5.0
motor==3.3.1
email-validator==2.2.0
pandas==2.2.0
```

Install command:
```bash
pip install -r streamlit_requirements.txt
```

##### 1.3 Environment Configuration
Create `.env.streamlit`:
```env
# Letta Configuration (User will provide)
LETTA_API_KEY=your_letta_api_key_here
LETTA_AGENT_ID=agent-xxx-xxx-xxx
LETTA_PROJECT_ID=project-xxx-xxx-xxx
LETTA_BASE_URL=https://api.letta.com  # or localhost:8283 for self-hosted

# MongoDB Configuration (Optional)
MONGO_URL=mongodb://localhost:27017
DB_NAME=talentscout_db

# Application Settings
APP_TITLE=TalentScout AI Hiring Assistant
APP_ICON=💼
DEBUG_MODE=False
```

##### 1.4 Create Base Streamlit App
Create `streamlit_app.py`:
```python
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('.env.streamlit')

# Page configuration
st.set_page_config(
    page_title=os.getenv('APP_TITLE', 'TalentScout AI Hiring Assistant'),
    page_icon=os.getenv('APP_ICON', '💼'),
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: right;
    }
    .assistant-message {
        background-color: #f5f5f5;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application entry point"""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 TalentScout AI Hiring Assistant</h1>', 
                unsafe_allow_html=True)
    st.markdown('---')
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Candidate Summary")
        st.info("Conversation not started yet.")
        
        st.markdown("---")
        st.subheader("ℹ️ About")
        st.write("""
        This AI assistant helps with initial candidate screening by:
        - Gathering essential information
        - Assessing technical skills
        - Generating relevant questions
        """)
    
    # Main chat interface (placeholder)
    st.subheader("💬 Chat Interface")
    
    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display placeholder message
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.write("👋 Hello! I'm ready to help screen candidates.")
            st.write("⚠️ **Note:** Letta agent integration pending.")
            st.write("Please provide your Letta API key, Agent ID, and Project ID.")
    
    # Chat input (placeholder)
    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Placeholder response
        with st.chat_message("assistant"):
            st.write("🔧 Letta integration coming in Phase 2!")

if __name__ == "__main__":
    main()
```

##### 1.5 Create Configuration Management
Create `config/settings.py`:
```python
import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    
    # Letta Configuration
    letta_api_key: str = "placeholder"
    letta_agent_id: str = "placeholder"
    letta_project_id: str = "placeholder"
    letta_base_url: str = "https://api.letta.com"
    
    # MongoDB Configuration
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "talentscout_db"
    
    # Application Settings
    app_title: str = "TalentScout AI Hiring Assistant"
    app_icon: str = "💼"
    debug_mode: bool = False
    
    class Config:
        env_file = ".env.streamlit"
        case_sensitive = False

# Global settings instance
settings = Settings()
```

##### 1.6 Create Utility Constants
Create `utils/constants.py`:
```python
from enum import Enum

class ConversationStage(Enum):
    """Conversation flow stages"""
    GREETING = "greeting"
    INFO_COLLECTION = "info_collection"
    TECH_STACK_DECLARATION = "tech_stack_declaration"
    TECHNICAL_QUESTIONS = "technical_questions"
    CONCLUSION = "conclusion"

class ExitKeywords:
    """Keywords to end conversation"""
    KEYWORDS = [
        "bye", "goodbye", "exit", "quit", 
        "end", "stop", "terminate", "finish"
    ]

class InfoFields:
    """Required information fields"""
    FULL_NAME = "full_name"
    EMAIL = "email"
    PHONE = "phone"
    YEARS_EXPERIENCE = "years_experience"
    DESIRED_POSITIONS = "desired_positions"
    CURRENT_LOCATION = "current_location"
    TECH_STACK = "tech_stack"

REQUIRED_FIELDS = [
    InfoFields.FULL_NAME,
    InfoFields.EMAIL,
    InfoFields.PHONE,
    InfoFields.YEARS_EXPERIENCE,
    InfoFields.DESIRED_POSITIONS,
    InfoFields.CURRENT_LOCATION,
    InfoFields.TECH_STACK
]
```

##### 1.7 Testing Phase 1
Create `tests/test_setup.py`:
```python
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Test if all required packages are installed"""
    try:
        import streamlit
        import pydantic
        from dotenv import load_dotenv
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")

def test_env_file_exists():
    """Test if .env.streamlit exists"""
    env_path = Path(__file__).parent.parent / '.env.streamlit'
    assert env_path.exists(), ".env.streamlit file not found"

def test_settings_load():
    """Test settings configuration"""
    from config.settings import settings
    assert settings.app_title is not None
    assert settings.letta_base_url is not None
```

Run tests:
```bash
pytest tests/test_setup.py -v
```

#### Deliverables
- ✅ Project folder structure created
- ✅ Dependencies installed
- ✅ Basic Streamlit app running
- ✅ Configuration management in place
- ✅ Constants and utilities defined
- ✅ Tests passing

#### How to Run Phase 1
```bash
cd /app
pip install -r streamlit_requirements.txt
streamlit run streamlit_app.py
```

Expected Output:
- Streamlit app opens in browser
- Shows placeholder chat interface
- Displays message that Letta integration is pending
- Sidebar shows empty candidate summary

---

### **PHASE 2: LETTA AGENT INTEGRATION**
**Duration:** 3-4 hours  
**Status:** ⏳ PENDING (After Phase 1)

#### Objectives
- Integrate Letta Python SDK
- Create agent service layer
- Initialize memory blocks
- Test agent communication

#### Tasks

##### 2.1 Create Letta Service
Create `services/letta_service.py`:
```python
from letta import Letta
from typing import Optional, Dict, List
import os
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

class LettaService:
    """Service for interacting with Letta Agent"""
    
    def __init__(self):
        """Initialize Letta client"""
        self.client: Optional[Letta] = None
        self.agent_id: str = settings.letta_agent_id
        self.is_connected: bool = False
    
    def connect(self) -> bool:
        """Connect to Letta API"""
        try:
            self.client = Letta(
                token=settings.letta_api_key,
                base_url=settings.letta_base_url
            )
            self.is_connected = True
            logger.info(f"Connected to Letta API at {settings.letta_base_url}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Letta: {e}")
            self.is_connected = False
            return False
    
    def send_message(self, message: str) -> Dict:
        """Send message to Letta agent and get response"""
        if not self.is_connected:
            raise ConnectionError("Letta client not connected")
        
        try:
            response = self.client.agents.messages.create(
                self.agent_id,
                messages=[{
                    "role": "user",
                    "content": message
                }]
            )
            return self._process_response(response)
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            return {"error": str(e)}
    
    def _process_response(self, response) -> Dict:
        """Process Letta agent response"""
        processed = {
            "messages": [],
            "memory_updates": []
        }
        
        for msg in response.messages:
            if hasattr(msg, 'content'):
                processed["messages"].append({
                    "role": msg.role,
                    "content": msg.content
                })
        
        return processed
    
    def get_memory_blocks(self) -> Dict:
        """Retrieve current memory blocks from agent"""
        # Implementation will use Letta API to fetch memory
        pass
    
    def update_memory(self, block_label: str, content: str) -> bool:
        """Update specific memory block"""
        # Implementation for manual memory updates if needed
        pass

# Global instance
letta_service = LettaService()
```

##### 2.2 Update Streamlit App with Letta Integration
Update `streamlit_app.py` to include:
```python
from services.letta_service import letta_service

# In main() function, add connection check:
if not letta_service.is_connected:
    if letta_service.connect():
        st.success("✅ Connected to Letta Agent!")
    else:
        st.error("❌ Failed to connect to Letta. Check your credentials.")
        st.stop()

# Replace placeholder chat with real Letta interaction
```

##### 2.3 Create Memory Block Initialization Script
Create `scripts/init_letta_agent.py`:
```python
"""
Script to initialize Letta agent with required memory blocks
Run this ONCE after getting Letta credentials
"""
from letta import Letta
from config.settings import settings

def create_hiring_assistant_agent():
    """Create a new Letta agent configured for hiring assistance"""
    
    client = Letta(token=settings.letta_api_key)
    
    # Define memory blocks
    memory_blocks = [
        {
            "label": "persona",
            "value": """
            Name: TalentScout AI Assistant
            Role: Professional hiring assistant for initial candidate screening
            Personality: Friendly, encouraging, professional, detail-oriented
            Mission: Gather candidate information and assess technical skills
            """
        },
        {
            "label": "human",
            "value": """
            Candidate Information:
            - Full Name: [Not provided]
            - Email: [Not provided]
            - Phone: [Not provided]
            - Years of Experience: [Not provided]
            - Desired Position(s): [Not provided]
            - Current Location: [Not provided]
            - Tech Stack: [Not provided]
            """
        },
        {
            "label": "conversation_state",
            "value": """
            Current Stage: greeting
            Information Collected: 0/7 fields
            Questions Asked: 0/5
            """
        },
        {
            "label": "guidelines",
            "value": """
            CRITICAL GUIDELINES:
            1. Stay focused on hiring assistant purpose - never deviate
            2. Collect all 7 required fields before moving to questions
            3. Generate 3-5 technical questions based on declared tech stack
            4. Validate email format (must contain @ and domain)
            5. Be conversational but maintain professionalism
            6. Handle unclear inputs gracefully with clarifying questions
            7. Detect exit keywords: bye, goodbye, exit, quit, end, stop
            8. Never ask for sensitive data beyond what's required
            """
        }
    ]
    
    # Create agent
    agent_state = client.agents.create(
        name="TalentScout Hiring Assistant",
        model="openai/gpt-4.1",  # or your preferred model
        memory_blocks=memory_blocks,
        tools=[]  # We'll add custom tools in Phase 3
    )
    
    print(f"✅ Agent created successfully!")
    print(f"Agent ID: {agent_state.id}")
    print(f"\nAdd this to your .env.streamlit file:")
    print(f"LETTA_AGENT_ID={agent_state.id}")
    
    return agent_state

if __name__ == "__main__":
    create_hiring_assistant_agent()
```

#### Deliverables
- ✅ Letta SDK integrated
- ✅ Service layer created
- ✅ Agent initialization script ready
- ✅ Connection testing implemented
- ✅ Basic message sending/receiving working

---

### **PHASE 3: CONVERSATION FLOW LOGIC**
**Duration:** 4-5 hours  
**Status:** ⏳ PENDING (After Phase 2)

#### Objectives
- Implement multi-stage conversation flow
- Add information collection logic
- Create validation mechanisms
- Handle fallback scenarios

#### Key Components
- Stage management (greeting → info collection → questions → conclusion)
- Field-by-field data gathering
- Input validation for email, phone, etc.
- Context-aware prompting
- Exit keyword detection

---

### **PHASE 4: TECHNICAL QUESTION GENERATION**
**Duration:** 3-4 hours  
**Status:** ⏳ PENDING (After Phase 3)

#### Objectives
- Parse tech stack declarations
- Generate relevant technical questions using Letta
- Ensure question quality and relevance
- Store questions and answers

#### Components
- Tech stack parser (extract languages, frameworks, tools)
- Prompt engineering for question generation
- Question difficulty adjustment based on experience
- Answer collection and storage

---

### **PHASE 5: UI/UX ENHANCEMENT**
**Duration:** 3-4 hours  
**Status:** ⏳ PENDING (After Phase 4)

#### Objectives
- Create polished chat interface
- Add candidate summary sidebar
- Implement progress indicators
- Add export functionality

#### Features
- Real-time typing indicators
- Message history display
- Candidate profile card in sidebar
- Download conversation transcript
- Export candidate data as JSON/CSV

---

### **PHASE 6: DATA PERSISTENCE & PRIVACY**
**Duration:** 2-3 hours  
**Status:** ⏳ PENDING (After Phase 5)

#### Objectives
- Implement data storage (MongoDB or JSON)
- Add GDPR compliance features
- Secure sensitive information
- Create data export/deletion functions

---

### **PHASE 7: TESTING & DEBUGGING**
**Duration:** 3-4 hours  
**Status:** ⏳ PENDING (After Phase 6)

#### Objectives
- Unit testing for all components
- Integration testing with Letta
- UI/UX testing
- Error handling verification

---

### **PHASE 8: DOCUMENTATION & DEMO**
**Duration:** 3-4 hours  
**Status:** ⏳ PENDING (After Phase 7)

#### Objectives
- Write comprehensive README
- Document prompt engineering strategies
- Create video demo
- Prepare deployment guide

---

## 📁 PROJECT STRUCTURE

```
/app/
│
├── streamlit_app.py                 # Main entry point
├── streamlit_requirements.txt       # Python dependencies
├── .env.streamlit                   # Environment configuration
├── .gitignore                       # Git ignore file
│
├── config/
│   ├── __init__.py
│   ├── settings.py                  # App settings
│   └── letta_config.py             # Letta configurations
│
├── services/
│   ├── __init__.py
│   ├── letta_service.py            # Letta agent interaction
│   ├── data_service.py             # Data persistence
│   └── validation_service.py       # Input validation
│
├── components/
│   ├── __init__.py
│   ├── chat_interface.py           # Chat UI
│   ├── sidebar.py                  # Sidebar components
│   └── conversation_display.py     # Message rendering
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py                  # Utility functions
│   └── constants.py                # Constants & enums
│
├── data/
│   └── candidates/                 # Stored candidate data
│
├── tests/
│   ├── __init__.py
│   ├── test_letta_service.py
│   ├── test_validation.py
│   └── test_conversation_flow.py
│
├── scripts/
│   └── init_letta_agent.py         # Agent initialization
│
└── docs/
    ├── README.md                    # Main documentation
    ├── PROMPT_ENGINEERING.md       # Prompt strategies
    ├── ARCHITECTURE.md             # Technical architecture
    └── DEPLOYMENT.md               # Deployment guide
```

---

## 🚀 GETTING STARTED

### Prerequisites
```bash
# Python 3.10 or higher
python --version

# Install dependencies
pip install -r streamlit_requirements.txt
```

### Environment Setup
1. Copy `.env.streamlit.example` to `.env.streamlit`
2. Add your Letta credentials:
   ```env
   LETTA_API_KEY=your_key_here
   LETTA_AGENT_ID=agent-xxx
   LETTA_PROJECT_ID=project-xxx
   ```

### Initialize Letta Agent (One-time)
```bash
python scripts/init_letta_agent.py
```

### Run Application
```bash
streamlit run streamlit_app.py
```

---

## ✅ SUCCESS CRITERIA

### Phase 1 Success
- ✅ Streamlit app runs without errors
- ✅ All dependencies installed
- ✅ Configuration loads correctly
- ✅ Basic UI structure displayed

### Overall Project Success
- ✅ Letta agent connects and responds
- ✅ All 7 information fields collected
- ✅ 3-5 relevant technical questions generated
- ✅ Conversation maintains context
- ✅ Fallback mechanisms work
- ✅ Data stored securely
- ✅ Exit keywords detected
- ✅ Comprehensive documentation
- ✅ Video demo created

---

## 📊 TIMELINE SUMMARY

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Phase 1: Setup | 2-3 hrs | 2-3 hrs |
| Phase 2: Letta Integration | 3-4 hrs | 5-7 hrs |
| Phase 3: Conversation Flow | 4-5 hrs | 9-12 hrs |
| Phase 4: Question Generation | 3-4 hrs | 12-16 hrs |
| Phase 5: UI/UX | 3-4 hrs | 15-20 hrs |
| Phase 6: Data & Privacy | 2-3 hrs | 17-23 hrs |
| Phase 7: Testing | 3-4 hrs | 20-27 hrs |
| Phase 8: Documentation | 3-4 hrs | 23-31 hrs |

**Total Estimated Time:** 23-31 hours (within 48-hour deadline)

---

## 🎯 NEXT STEPS

1. **Review this implementation plan**
2. **Confirm you have Letta credentials** (API key, Agent ID, Project ID)
3. **Proceed with Phase 1 implementation**
4. **Test each phase before moving to next**

---

## 📝 NOTES

- **Letta Integration:** Phase 2 requires valid Letta credentials
- **Testing:** Each phase includes testing checkpoints
- **Flexibility:** Plan can be adjusted based on user feedback
- **Documentation:** README will be comprehensive and detailed

---

**Ready to start Phase 1? Let's build this! 🚀**
