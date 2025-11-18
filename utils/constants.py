"""Constants and enumerations for the application"""
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

# Tech stack categories
TECH_STACK_CATEGORIES = {
    "languages": ["Python", "JavaScript", "Java", "C++", "Go", "Ruby", "PHP", "TypeScript"],
    "frameworks": ["React", "Angular", "Vue", "Django", "Flask", "FastAPI", "Spring", "Express"],
    "databases": ["MongoDB", "PostgreSQL", "MySQL", "Redis", "Cassandra", "DynamoDB"],
    "tools": ["Docker", "Kubernetes", "Git", "Jenkins", "AWS", "Azure", "GCP"]
}
