"""Test Phase 1 setup and configuration"""
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
    assert settings.app_icon is not None

def test_constants():
    """Test constants are properly defined"""
    from utils.constants import ConversationStage, ExitKeywords, REQUIRED_FIELDS
    
    assert len(REQUIRED_FIELDS) == 7
    assert "bye" in ExitKeywords.KEYWORDS
    assert ConversationStage.GREETING.value == "greeting"

def test_helpers():
    """Test helper functions"""
    from utils.helpers import validate_email, validate_phone, is_exit_keyword
    
    # Test email validation
    assert validate_email("test@example.com") == True
    assert validate_email("invalid-email") == False
    
    # Test phone validation
    assert validate_phone("+1234567890") == True
    assert validate_phone("123") == False
    
    # Test exit keyword detection
    assert is_exit_keyword("bye") == True
    assert is_exit_keyword("hello") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
