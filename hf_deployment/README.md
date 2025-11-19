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

## Features

- 🤖 Real-time AI conversation with streaming responses
- 💭 Reasoning messages displayed in italic
- 🔧 Tool calls tracking
- 📊 Conversation statistics
- 🎨 ChatGPT-style dark theme interface

## Configuration

This app requires the following environment variables (configure in Settings > Secrets):

```
LETTA_API_KEY=your_letta_api_key
LETTA_AGENT_ID=your_agent_id
LETTA_PROJECT_ID=your_project_id
LETTA_BASE_URL=https://api.letta.com
APP_TITLE=TalentScout AI Hiring Assistant
APP_ICON=💼
DEBUG_MODE=False
```

## How to Use

1. Once the app loads, it will automatically connect to your Letta AI agent
2. Start typing your message in the chat input
3. Watch the AI respond in real-time with streaming
4. Reasoning messages appear in italic before the main response

## About Letta

This app uses [Letta](https://www.letta.com/) for AI agent orchestration with memory and tool calling capabilities.

## License

MIT License