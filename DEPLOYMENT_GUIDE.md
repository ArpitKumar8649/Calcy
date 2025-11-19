# 🚀 Deploying TalentScout to Hugging Face Spaces

## Step-by-Step Deployment Guide

### Step 1: Prepare Your Repository

Your app is now ready for deployment! The following files have been created:

- ✅ `requirements.txt` - Python dependencies
- ✅ `README.md` - Hugging Face Space metadata and description
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `streamlit_app.py` - Main application file
- ✅ All supporting files (config/, services/, utils/, components/)

### Step 2: Create a Hugging Face Account

1. Go to [huggingface.co](https://huggingface.co)
2. Sign up for a free account (if you don't have one)
3. Verify your email

### Step 3: Create a New Space

1. Click on your profile picture → **"New Space"**
2. Fill in the details:
   - **Space name**: `talentscout-ai-hiring` (or your preferred name)
   - **License**: MIT
   - **Select SDK**: Choose **Streamlit**
   - **Space hardware**: CPU basic (free tier)
   - **Visibility**: Public or Private (your choice)
3. Click **"Create Space"**

### Step 4: Upload Your Files

You have two options:

#### Option A: Git Push (Recommended)

1. In your terminal, navigate to `/app` directory
2. Initialize git (if not already done):
   ```bash
   git init
   git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   ```
3. Add and commit files:
   ```bash
   git add streamlit_app.py requirements.txt README.md
   git add .streamlit/ config/ services/ utils/ components/
   git commit -m "Initial commit: TalentScout AI Hiring Assistant"
   ```
4. Push to Hugging Face:
   ```bash
   git push hf main
   ```

#### Option B: Web Interface Upload

1. Go to your newly created Space
2. Click **"Files"** tab
3. Click **"Add file"** → **"Upload files"**
4. Upload these files and folders:
   - `streamlit_app.py`
   - `requirements.txt`
   - `README.md`
   - `.streamlit/` folder
   - `config/` folder
   - `services/` folder
   - `utils/` folder
   - `components/` folder

### Step 5: Configure Secrets (IMPORTANT!)

Your app needs Letta API credentials to work. Configure them as secrets:

1. Go to your Space settings → **"Settings"** tab
2. Scroll down to **"Repository secrets"**
3. Click **"Add a secret"** and add each of these:

```
LETTA_API_KEY = sk-let-MGE1NDZmY2MtZGUzZS00N2Q2LTg4YTYtYTgyOGJhOTA2MDI5OjdhZmYyMGNkLTY4NTAtNDczYS04Njc0LWJmM2QwZWI0MDBhNQ==
LETTA_AGENT_ID = agent-d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7
LETTA_PROJECT_ID = project-decoder-1
LETTA_BASE_URL = https://api.letta.com
APP_TITLE = TalentScout AI Hiring Assistant
APP_ICON = 💼
DEBUG_MODE = False
```

> ⚠️ **Important**: Add each secret one by one. The secret names must match exactly.

### Step 6: Wait for Build

1. Hugging Face will automatically detect the Streamlit SDK
2. It will install dependencies from `requirements.txt`
3. Wait 2-3 minutes for the build to complete
4. The app will automatically start running

### Step 7: Test Your App

1. Once the build completes, your app will be live!
2. The URL will be: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`
3. Test the typing effect on "TalentScout" when the page loads
4. Try chatting with the AI assistant

## Files to Upload Summary

**Required files:**
- `streamlit_app.py` - Main app
- `requirements.txt` - Dependencies
- `README.md` - Space description
- `.streamlit/config.toml` - Streamlit settings

**Required folders:**
- `config/` - Settings and configuration
- `services/` - Letta service integration
- `utils/` - Helper utilities
- `components/` - UI components

**DO NOT upload:**
- `.env.streamlit` (use Secrets instead)
- `backend/` folder (not needed for Streamlit)
- `frontend/` folder (React app, not needed)
- `node_modules/`
- `.git/` folder
- `__pycache__/`

## Troubleshooting

### App Not Starting?
- Check the "Logs" tab in your Space
- Verify all secrets are configured correctly
- Ensure `requirements.txt` was uploaded

### Connection Error?
- Verify your Letta API key is valid
- Check that LETTA_AGENT_ID matches your agent

### Missing Dependencies?
- Check the build logs
- Ensure `requirements.txt` includes all packages

## Optional: Custom Domain

After deployment, you can:
1. Share the public URL
2. Embed the Space in a website
3. Use the Hugging Face API to interact with your app

## Need Help?

- Hugging Face Docs: https://huggingface.co/docs/hub/spaces
- Streamlit Docs: https://docs.streamlit.io/
- Letta Docs: https://docs.letta.com/

---

Good luck with your deployment! 🎉
