"""Application settings and configuration management"""
import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Letta Configuration
    letta_api_key: str = "placeholder"
    letta_agent_id: str = "placeholder"
    letta_project_id: str = "placeholder"
    letta_base_url: str = "https://api.letta.com"
    
    # MongoDB Configuration (Optional)
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "talentscout_db"
    
    # Application Settings
    app_title: str = "TalentScout AI Hiring Assistant"
    app_icon: str = "💼"
    debug_mode: bool = False
    
    class Config:
        env_file = ".env.streamlit"
        case_sensitive = False
        extra = "allow"

# Global settings instance
settings = Settings()
