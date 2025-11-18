"""Helper utility functions"""
import re
from typing import Dict, List, Optional
import json
from datetime import datetime
from utils.constants import ExitKeywords

def is_exit_keyword(text: str) -> bool:
    """Check if user input contains exit keywords"""
    text_lower = text.lower().strip()
    return any(keyword in text_lower for keyword in ExitKeywords.KEYWORDS)

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate phone number (basic validation)"""
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
    # Check if it's 10-15 digits
    return bool(re.match(r'^\+?\d{10,15}$', cleaned))

def extract_tech_stack(text: str) -> Dict[str, List[str]]:
    """Extract tech stack from user input"""
    # This is a simple extraction - can be enhanced with NLP
    from utils.constants import TECH_STACK_CATEGORIES
    
    extracted = {
        "languages": [],
        "frameworks": [],
        "databases": [],
        "tools": [],
        "other": []
    }
    
    text_lower = text.lower()
    
    for category, items in TECH_STACK_CATEGORIES.items():
        for item in items:
            if item.lower() in text_lower:
                extracted[category].append(item)
    
    return extracted

def save_candidate_data(candidate_data: Dict, filepath: str) -> bool:
    """Save candidate data to JSON file"""
    try:
        candidate_data['timestamp'] = datetime.now().isoformat()
        with open(filepath, 'w') as f:
            json.dump(candidate_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving candidate data: {e}")
        return False

def load_candidate_data(filepath: str) -> Optional[Dict]:
    """Load candidate data from JSON file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading candidate data: {e}")
        return None

def format_conversation_history(messages: List[Dict]) -> str:
    """Format conversation history for display"""
    formatted = []
    for msg in messages:
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        formatted.append(f"{role.upper()}: {content}")
    return "\n\n".join(formatted)
