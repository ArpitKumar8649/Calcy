---
title: TalentScout AI Hiring Assistant
emoji: 💼
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.32.0
app_file: streamlit_app.py
pinned: false
license: mit
---

# TalentScout AI Hiring Assistant 💼

An AI-powered hiring assistant chatbot built with Letta AI and Streamlit.

## 🌟 Features

- 🤖 **Real-time AI conversation** with streaming responses
- 💭 **Reasoning messages** displayed in italic
- 🔧 **Tool calls tracking** for transparency
- 📊 **Conversation statistics** and monitoring
- 🎨 **ChatGPT-style dark theme** interface
- ⚡ **Token-level streaming** for instant feedback
- 🔄 **Conversation history** with session management

## 🚀 Quick Deploy to Streamlit Cloud

### Option 1: Use This Template (Fastest)

1. Click **"Use this template"** on GitHub
2. Go to https://share.streamlit.io
3. Click **"New app"** and select your repository
4. Add secrets (see Configuration below)
5. Deploy! 🎉

### Option 2: Deploy Your Own Fork

See detailed instructions in [QUICK_START.md](QUICK_START.md) or [STREAMLIT_DEPLOYMENT_GUIDE.md](STREAMLIT_DEPLOYMENT_GUIDE.md)

## ⚙️ Configuration

This app requires the following secrets (configure in Streamlit Cloud Settings > Secrets):

```toml
# Letta Configuration
LETTA_API_KEY = "your_letta_api_key"
LETTA_AGENT_ID = "agent-xxx-xxx-xxx"
LETTA_PROJECT_ID = "proj-xxx-xxx-xxx"
LETTA_BASE_URL = "https://api.letta.com"

# Application Settings (Optional)
APP_TITLE = "TalentScout AI Hiring Assistant"
APP_ICON = "💼"
DEBUG_MODE = false
```

### Where to Get Credentials

1. **Letta API Key**: https://app.letta.com/ → Settings → API Keys
2. **Agent ID**: https://app.letta.com/ → Agents → Select your agent → Copy ID
3. **Project ID**: https://app.letta.com/ → Projects → Copy your project ID

## 💻 Local Development

### Prerequisites

- Python 3.9+
- Letta account and API credentials

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env.streamlit file
cp .env.streamlit.example .env.streamlit

# 5. Edit .env.streamlit with your credentials
nano .env.streamlit  # or use your preferred editor

# 6. Run the app
streamlit run streamlit_app.py
```

The app will open at http://localhost:8501

## 📖 How to Use

1. **Launch**: Once the app loads, it automatically connects to your Letta AI agent
2. **Chat**: Start typing your message in the chat input at the bottom
3. **Watch**: See the AI respond in real-time with streaming
4. **Reasoning**: Reasoning messages appear in italic before the main response
5. **History**: Scroll through conversation history
6. **Reset**: Click "New Conversation" to start fresh

## 🏗️ Project Structure

```
.
├── streamlit_app.py              # Main application
├── requirements.txt              # Python dependencies
├── config/
│   └── settings.py              # Configuration management
├── services/
│   └── letta_service.py         # Letta AI integration
├── utils/
│   ├── constants.py             # Constants and enums
│   └── helpers.py               # Helper functions
└── docs/
    ├── QUICK_START.md           # 5-minute deployment guide
    ├── STREAMLIT_DEPLOYMENT_GUIDE.md  # Detailed guide
    └── DEPLOYMENT_CHECKLIST.md  # Deployment checklist
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit 1.32.0+
- **AI Agent**: Letta AI with streaming support
- **Language**: Python 3.9+
- **Styling**: Custom CSS (ChatGPT-inspired dark theme)

## 🔧 Dependencies

All dependencies are managed in `requirements.txt`:
- `streamlit` - Web framework
- `letta-client` - Letta AI Python client
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation
- And more...

## 📚 Documentation

- [Quick Start Guide](QUICK_START.md) - Deploy in 5 minutes
- [Detailed Deployment Guide](STREAMLIT_DEPLOYMENT_GUIDE.md) - Step-by-step instructions
- [Deployment Checklist](DEPLOYMENT_CHECKLIST.md) - Track your deployment progress

## 🤝 About Letta

This app uses [Letta](https://www.letta.com/) for AI agent orchestration with:
- **Memory**: Persistent conversation context
- **Tool calling**: Agent can use tools and functions
- **Streaming**: Real-time response generation
- **Reasoning**: Internal thought process visibility

Learn more at [docs.letta.com](https://docs.letta.com)

## 🐛 Troubleshooting

### App shows "Connection Error"
- Verify your Letta credentials in Streamlit Secrets
- Check that API key starts with `lm-`
- Ensure Agent ID format is `agent-xxx-xxx-xxx`

### Module import errors
- All dependencies should be in `requirements.txt`
- Streamlit auto-installs on deployment
- Check deployment logs for specific errors

### Streaming not working
- Verify you're using `letta-client>=0.1.324`
- Check Letta service status at https://status.letta.com

For more help, see [STREAMLIT_DEPLOYMENT_GUIDE.md](STREAMLIT_DEPLOYMENT_GUIDE.md)

## 📄 License

MIT License - feel free to use this for your own projects!

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Powered by [Letta AI](https://www.letta.com)
- Inspired by ChatGPT's interface design

---

**Ready to deploy?** Start with [QUICK_START.md](QUICK_START.md) 🚀