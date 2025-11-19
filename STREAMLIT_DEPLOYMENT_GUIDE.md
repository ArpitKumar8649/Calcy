# 🚀 Streamlit Community Cloud Deployment Guide

## Complete Step-by-Step Guide to Deploy TalentScout AI Hiring Assistant

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Prepare Your Repository](#step-1-prepare-your-repository)
3. [Push to GitHub](#step-2-push-to-github)
4. [Deploy on Streamlit Community Cloud](#step-3-deploy-on-streamlit-community-cloud)
5. [Configure Secrets](#step-4-configure-secrets)
6. [Verify Deployment](#step-5-verify-deployment)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, make sure you have:

- ✅ **GitHub Account** - Sign up at https://github.com
- ✅ **Streamlit Community Cloud Account** - Sign up at https://share.streamlit.io
- ✅ **Letta AI Account** - Get your API credentials from https://app.letta.com
- ✅ **Git installed** on your local machine
- ✅ **Your Letta credentials**:
  - API Key
  - Agent ID
  - Project ID

---

## Step 1: Prepare Your Repository

### 1.1 Verify File Structure

Ensure your repository has this structure:

```
/app/
├── streamlit_app.py              # Main application ✅
├── streamlit_requirements.txt     # Python dependencies ✅
├── README.md                      # Project documentation ✅
├── .env.streamlit.example         # Environment variables template ✅
├── config/
│   ├── __init__.py
│   └── settings.py               # Configuration (Updated for Cloud) ✅
├── services/
│   ├── __init__.py
│   └── letta_service.py          # Letta AI integration ✅
└── utils/
    ├── __init__.py
    ├── constants.py
    └── helpers.py
```

### 1.2 Check Required Files

Run these commands to verify all files exist:

```bash
# Navigate to your app directory
cd /app

# Check if main files exist
ls -la streamlit_app.py
ls -la streamlit_requirements.txt
ls -la README.md

# Check if folders exist
ls -la config/
ls -la services/
ls -la utils/
```

### 1.3 Review Dependencies

Your `streamlit_requirements.txt` should contain:

```
streamlit>=1.32.0
letta-client>=0.1.324
python-dotenv>=1.0.1
pydantic>=2.12.0
pydantic-settings>=2.2.1
pymongo>=4.5.0
motor>=3.3.1
email-validator>=2.2.0
pandas>=2.2.0
pytest>=8.0.0
```

✅ **Already configured correctly!**

---

## Step 2: Push to GitHub

### 2.1 Create a New GitHub Repository

1. Go to https://github.com/new
2. **Repository name**: `talentscout-ai-assistant` (or your preferred name)
3. **Description**: "AI-powered hiring assistant with Letta AI and Streamlit"
4. **Visibility**: Choose **Public** or **Private**
5. ✅ **DO NOT** initialize with README (we already have one)
6. Click **"Create repository"**

### 2.2 Initialize Git (if not already done)

```bash
# Navigate to your app directory
cd /app

# Initialize git if not already initialized
git init

# Check git status
git status
```

### 2.3 Create .gitignore File

Create a `.gitignore` file to exclude sensitive files:

```bash
cat > .gitignore << 'EOF'
# Environment files with secrets
.env
.env.streamlit
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# Streamlit
.streamlit/secrets.toml

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite
EOF
```

### 2.4 Add and Commit Files

```bash
# Add all files
git add .

# Commit with a message
git commit -m "Initial commit: TalentScout AI Hiring Assistant"

# Verify commit
git log --oneline
```

### 2.5 Push to GitHub

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values:

```bash
# Set main branch
git branch -M main

# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

**Example**:
```bash
git remote add origin https://github.com/johndoe/talentscout-ai-assistant.git
git push -u origin main
```

### 2.6 Verify on GitHub

1. Go to your repository URL: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
2. Verify all files are uploaded
3. Check that `.env.streamlit` is **NOT** visible (it should be gitignored)

---

## Step 3: Deploy on Streamlit Community Cloud

### 3.1 Sign In to Streamlit Community Cloud

1. Go to https://share.streamlit.io
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub account

### 3.2 Create New App

1. Click the **"New app"** button (top right)
2. You'll see a deployment form

### 3.3 Fill in Deployment Settings

**Repository Configuration**:

| Field | Value | Example |
|-------|-------|---------|
| **Repository** | `YOUR_USERNAME/YOUR_REPO_NAME` | `johndoe/talentscout-ai-assistant` |
| **Branch** | `main` | `main` |
| **Main file path** | `streamlit_app.py` | `streamlit_app.py` |

**Important Notes**:
- If your `streamlit_app.py` is in a subdirectory like `/app/`, use: `app/streamlit_app.py`
- If it's in the root, just use: `streamlit_app.py`

**App URL** (optional):
- Choose a custom URL: `https://YOUR-APP-NAME.streamlit.app`
- Example: `https://talentscout-ai.streamlit.app`

### 3.4 Advanced Settings (Optional)

Click **"Advanced settings"** if you need to:
- Set Python version (default is usually fine)
- Specify requirements file location (if not in root)

---

## Step 4: Configure Secrets

⚠️ **CRITICAL STEP**: Your app needs API credentials to work!

### 4.1 Access Secrets Manager

1. After clicking "Deploy", you'll see your app dashboard
2. Click on **"Settings"** (⚙️ icon)
3. Select **"Secrets"** from the left menu

### 4.2 Add Your Secrets

Copy and paste this template, replacing with your **actual values**:

```toml
# Letta Configuration
LETTA_API_KEY = "lm-xxxxxxxxxxxxxxxxxxxxxxxx"
LETTA_AGENT_ID = "agent-d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7"
LETTA_PROJECT_ID = "proj-xxxxxxxxxxxxxxxx"
LETTA_BASE_URL = "https://api.letta.com"

# Application Settings
APP_TITLE = "TalentScout AI Hiring Assistant"
APP_ICON = "💼"
DEBUG_MODE = false
```

### 4.3 Where to Get Letta Credentials

1. **Letta API Key**:
   - Go to https://app.letta.com/
   - Navigate to **Settings** → **API Keys**
   - Click **"Create new API key"**
   - Copy the key (starts with `lm-`)

2. **Agent ID**:
   - Go to **Agents** section in Letta dashboard
   - Click on your agent
   - Copy the Agent ID from the URL or details page
   - Format: `agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

3. **Project ID**:
   - In Letta dashboard, check your project settings
   - Copy the Project ID
   - Format: `proj-xxxxxxxx` or similar

### 4.4 Save Secrets

1. Click **"Save"** button
2. Wait for the app to restart automatically

---

## Step 5: Verify Deployment

### 5.1 Wait for Deployment

- Streamlit will install dependencies (takes 2-5 minutes)
- Watch the deployment logs in the dashboard
- You'll see:
  ```
  ✓ Installing dependencies...
  ✓ Building application...
  ✓ Starting app...
  ```

### 5.2 Check App Status

Your app should show:
- **Status**: 🟢 Running
- **URL**: `https://your-app-name.streamlit.app`

### 5.3 Test Your App

1. Click on the app URL
2. The app should load with:
   - ✅ "TalentScout AI Hiring Assistant" header
   - ✅ "AI Agent Connected" status in sidebar
   - ✅ Agent information displayed
   - ✅ Chat input ready

3. Test the chat:
   - Type: "Hello"
   - Watch for streaming response
   - Verify reasoning messages appear in italic
   - Check that responses are coherent

### 5.4 Verify Letta Connection

In the sidebar, you should see:
- ✅ **AI Agent Connected** (green badge)
- ✅ **Agent ID**: Your agent ID
- ✅ **Model**: gpt-5-mini (or your model)
- ✅ **Agent Name**: Your agent name

---

## Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'X'"

**Cause**: Missing dependency in requirements file

**Solution**:
1. Add the missing package to `streamlit_requirements.txt`
2. Commit and push:
   ```bash
   git add streamlit_requirements.txt
   git commit -m "Add missing dependency"
   git push
   ```
3. Streamlit will auto-redeploy

### Issue 2: "Connection Error" / "Failed to connect to Letta"

**Cause**: Incorrect or missing Letta credentials

**Solution**:
1. Verify secrets in Streamlit dashboard
2. Check that API key is correct (no extra spaces)
3. Ensure Agent ID format is correct: `agent-xxx-xxx-xxx`
4. Test credentials locally first:
   ```bash
   cd /app
   streamlit run streamlit_app.py
   ```

### Issue 3: "File not found: streamlit_app.py"

**Cause**: Incorrect main file path in deployment settings

**Solution**:
1. Go to app settings in Streamlit Cloud
2. Update **Main file path**:
   - If in root: `streamlit_app.py`
   - If in /app/: `app/streamlit_app.py`
3. Click "Save" and redeploy

### Issue 4: App Stuck on "Starting..."

**Cause**: Code error or infinite loop

**Solution**:
1. Check deployment logs for errors
2. Look for Python tracebacks
3. Fix the error in your code
4. Push update to GitHub:
   ```bash
   git add .
   git commit -m "Fix deployment error"
   git push
   ```

### Issue 5: "Secrets not found"

**Cause**: Secrets not configured or wrong format

**Solution**:
1. Verify secrets are in TOML format (not JSON or ENV)
2. Check for syntax errors (missing quotes, wrong brackets)
3. Ensure no trailing commas
4. Save secrets and restart app

### Issue 6: Import Errors (e.g., "cannot import name 'settings'")

**Cause**: Incorrect Python path or module structure

**Solution**:
1. Ensure all folders have `__init__.py` files:
   ```bash
   touch config/__init__.py
   touch services/__init__.py
   touch utils/__init__.py
   ```
2. Commit and push:
   ```bash
   git add .
   git commit -m "Add __init__.py files"
   git push
   ```

---

## Testing Locally Before Deployment

### Test with Streamlit CLI

```bash
# Navigate to app directory
cd /app

# Set environment variables (or use .env.streamlit)
export LETTA_API_KEY="your_key"
export LETTA_AGENT_ID="your_agent_id"
export LETTA_PROJECT_ID="your_project_id"

# Run Streamlit locally
streamlit run streamlit_app.py

# Open browser to http://localhost:8501
```

### Test with Docker (Optional)

```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY streamlit_requirements.txt .
RUN pip install -r streamlit_requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
EOF

# Build and run
docker build -t talentscout-app .
docker run -p 8501:8501 --env-file .env.streamlit talentscout-app
```

---

## Updating Your Deployed App

### Make Changes and Redeploy

```bash
# 1. Make your changes to the code
# 2. Test locally
streamlit run streamlit_app.py

# 3. Commit changes
git add .
git commit -m "Update: description of changes"

# 4. Push to GitHub
git push

# 5. Streamlit will auto-redeploy (takes 2-3 minutes)
```

### Update Secrets

1. Go to Streamlit dashboard
2. Settings → Secrets
3. Update values
4. Click Save
5. App will restart automatically

---

## Best Practices

### Security

- ✅ Never commit `.env` files with real credentials
- ✅ Use Streamlit Secrets for all API keys
- ✅ Keep `.gitignore` updated
- ✅ Rotate API keys regularly

### Performance

- ✅ Use `@st.cache_data` for data loading
- ✅ Use `@st.cache_resource` for model/client initialization
- ✅ Minimize API calls in loops

### Monitoring

- ✅ Check app analytics in Streamlit dashboard
- ✅ Monitor deployment logs for errors
- ✅ Set up error notifications

---

## Additional Resources

- **Streamlit Documentation**: https://docs.streamlit.io
- **Streamlit Community Cloud**: https://docs.streamlit.io/streamlit-community-cloud
- **Letta Documentation**: https://docs.letta.com
- **GitHub Help**: https://docs.github.com

---

## Support

If you encounter issues not covered in this guide:

1. Check Streamlit Community Forum: https://discuss.streamlit.io
2. Review deployment logs in Streamlit dashboard
3. Test locally to isolate the issue
4. Check Letta API status: https://status.letta.com

---

## Summary Checklist

Before deployment, verify:

- [ ] All code pushed to GitHub
- [ ] `.env` files excluded from git
- [ ] `streamlit_requirements.txt` is complete
- [ ] All imports are correct
- [ ] Letta credentials obtained
- [ ] GitHub account connected to Streamlit Cloud
- [ ] Repository is public (or Streamlit has access to private repo)

During deployment:

- [ ] Repository, branch, and file path are correct
- [ ] Secrets configured in TOML format
- [ ] All required secrets added
- [ ] Deployment logs show no errors

After deployment:

- [ ] App URL loads successfully
- [ ] Letta agent connects
- [ ] Chat functionality works
- [ ] Streaming responses appear
- [ ] No console errors

---

🎉 **Congratulations!** Your TalentScout AI Hiring Assistant is now deployed on Streamlit Community Cloud!

Your app is accessible at: `https://your-app-name.streamlit.app`

Share the link and start interviewing candidates with AI! 🚀
