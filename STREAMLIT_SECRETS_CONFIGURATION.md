# 🔐 Streamlit Secrets Configuration

## Exact Configuration for Your App

When you deploy to Streamlit Community Cloud, you'll see a **Secrets** section in Advanced Settings. This guide shows you **exactly** what to paste there.

---

## 📋 What You'll See in Streamlit Dashboard

```
Advanced settings
Python version
3.13  (or 3.11, 3.12 - any is fine)

Secrets
Provide environment variables and other secrets to your app 
using TOML format. This information is encrypted and served 
securely to your app at runtime.
```

---

## ✅ What to Paste in the Secrets Box

### Option 1: With Your Actual Letta Credentials

Copy this template and **replace** the placeholder values with your actual credentials:

```toml
# Letta AI Configuration (REQUIRED)
LETTA_API_KEY = "lm-your-actual-api-key-here"
LETTA_AGENT_ID = "agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
LETTA_PROJECT_ID = "proj-your-project-id-here"
LETTA_BASE_URL = "https://api.letta.com"

# Application Settings (OPTIONAL - you can customize these)
APP_TITLE = "TalentScout AI Hiring Assistant"
APP_ICON = "💼"
DEBUG_MODE = false
```

### Option 2: Example with Real Format

Here's an example showing the correct format (with fake credentials):

```toml
# Letta AI Configuration
LETTA_API_KEY = "lm-abcdef1234567890"
LETTA_AGENT_ID = "agent-d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7"
LETTA_PROJECT_ID = "proj-a1b2c3d4e5f6"
LETTA_BASE_URL = "https://api.letta.com"

# Application Settings
APP_TITLE = "TalentScout AI Hiring Assistant"
APP_ICON = "💼"
DEBUG_MODE = false
```

---

## 🔍 Where to Get Your Credentials

### 1. LETTA_API_KEY

1. Go to: **https://app.letta.com/**
2. Click on **Settings** (⚙️) in the left sidebar
3. Navigate to **API Keys**
4. Click **"Create new API key"** or copy existing one
5. Copy the key (it starts with `lm-`)
6. Example format: `lm-abc123def456...`

### 2. LETTA_AGENT_ID

1. Go to: **https://app.letta.com/**
2. Click on **Agents** in the left sidebar
3. Click on your agent (e.g., "memory-agent_copy")
4. Copy the **Agent ID** from the URL or details page
5. Format: `agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
6. Example: `agent-d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7`

### 3. LETTA_PROJECT_ID

1. Go to: **https://app.letta.com/**
2. Check your **Project** section or settings
3. Copy your **Project ID**
4. Format varies, but typically: `proj-xxxxxxxxx`

---

## ⚠️ Important Notes

### TOML Format Rules

✅ **DO**:
- Use double quotes `"` for string values
- Use lowercase `true`/`false` for booleans (not `True`/`False`)
- Keep one value per line
- Use `=` to assign values
- Comments start with `#`

❌ **DON'T**:
- Don't use single quotes `'`
- Don't use Python-style `True`/`False`
- Don't add trailing commas
- Don't add semicolons
- Don't forget the `=` sign

### Correct vs Incorrect Examples

✅ **CORRECT**:
```toml
LETTA_API_KEY = "lm-abc123"
DEBUG_MODE = false
APP_ICON = "💼"
```

❌ **INCORRECT**:
```toml
LETTA_API_KEY = 'lm-abc123'  # Single quotes - wrong!
DEBUG_MODE = False            # Capital F - wrong!
APP_ICON = 💼                 # No quotes - wrong!
```

---

## 🎯 Minimal Configuration (Just What's Required)

If you want the absolute minimum, paste just these 4 lines:

```toml
LETTA_API_KEY = "your-api-key"
LETTA_AGENT_ID = "your-agent-id"
LETTA_PROJECT_ID = "your-project-id"
LETTA_BASE_URL = "https://api.letta.com"
```

The app will use default values for everything else.

---

## 🎨 Custom Configuration Examples

### Change the App Title and Icon

```toml
LETTA_API_KEY = "your-api-key"
LETTA_AGENT_ID = "your-agent-id"
LETTA_PROJECT_ID = "your-project-id"
LETTA_BASE_URL = "https://api.letta.com"

# Customize your app
APP_TITLE = "My Custom Hiring Bot"
APP_ICON = "🤖"
```

### Enable Debug Mode

```toml
LETTA_API_KEY = "your-api-key"
LETTA_AGENT_ID = "your-agent-id"
LETTA_PROJECT_ID = "your-project-id"
LETTA_BASE_URL = "https://api.letta.com"

DEBUG_MODE = true
```

---

## 📝 Step-by-Step Configuration Process

### Step 1: Open Secrets Editor

1. Deploy your app on Streamlit Cloud
2. Go to your app dashboard
3. Click **"Settings"** (⚙️ icon)
4. Click **"Secrets"** in the left menu
5. You'll see a text editor

### Step 2: Gather Your Credentials

Open **https://app.letta.com/** in another tab and collect:
- [ ] API Key
- [ ] Agent ID  
- [ ] Project ID

### Step 3: Paste Configuration

In the Secrets editor, paste this template:

```toml
LETTA_API_KEY = "paste-your-key-here"
LETTA_AGENT_ID = "paste-your-agent-id-here"
LETTA_PROJECT_ID = "paste-your-project-id-here"
LETTA_BASE_URL = "https://api.letta.com"
```

### Step 4: Replace Placeholders

Replace each placeholder with your actual values:
- `paste-your-key-here` → your actual API key
- `paste-your-agent-id-here` → your actual agent ID
- `paste-your-project-id-here` → your actual project ID

### Step 5: Save

1. Click the **"Save"** button
2. Wait ~60 seconds for changes to propagate
3. Your app will restart automatically

---

## ✅ Verification Checklist

After saving secrets, verify:

- [ ] No syntax errors shown in the editor
- [ ] All values have double quotes
- [ ] Boolean values are lowercase (`true`/`false`)
- [ ] No trailing commas or semicolons
- [ ] Secrets saved successfully (green checkmark)
- [ ] App restarted (check status indicator)

---

## 🐛 Common Mistakes and Fixes

### Mistake 1: Missing Quotes

**Wrong**:
```toml
LETTA_API_KEY = lm-abc123
```

**Right**:
```toml
LETTA_API_KEY = "lm-abc123"
```

### Mistake 2: Single Quotes

**Wrong**:
```toml
LETTA_API_KEY = 'lm-abc123'
```

**Right**:
```toml
LETTA_API_KEY = "lm-abc123"
```

### Mistake 3: Python-style Booleans

**Wrong**:
```toml
DEBUG_MODE = True
```

**Right**:
```toml
DEBUG_MODE = true
```

### Mistake 4: Extra Spaces in Keys

**Wrong**:
```toml
LETTA_API_KEY = "lm-abc123 "  # Space at end
```

**Right**:
```toml
LETTA_API_KEY = "lm-abc123"
```

### Mistake 5: Wrong Agent ID Format

**Wrong**:
```toml
LETTA_AGENT_ID = "d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7"  # Missing "agent-" prefix
```

**Right**:
```toml
LETTA_AGENT_ID = "agent-d1d5bea5-542a-4be1-a7f8-b2b8d95c9be7"
```

---

## 🔍 Testing Your Configuration

After saving secrets, test your app:

### 1. Check Connection Status

Look at the sidebar:
- ✅ Should show: **"AI Agent Connected"** (green)
- ❌ If shows: **"Connection Error"** (red) → Check your credentials

### 2. Verify Agent Info

The sidebar should display:
- Agent ID: `agent-xxx...`
- Model: `gpt-5-mini` (or your model)
- Agent Name: Your agent's name

### 3. Test Chat

1. Type a message: "Hello"
2. Press Enter
3. Should see:
   - Thinking indicator (animated dots)
   - Reasoning message in italic
   - Assistant response

---

## 📊 Python Version Selection

In the same Advanced Settings, you can choose Python version:

**Recommended**: `3.11` or `3.12`

- ✅ `3.11` - Stable, well-tested
- ✅ `3.12` - Latest stable, recommended
- ⚠️ `3.13` - Very new, may have compatibility issues

**Our app works with**: Python 3.9+ (any version is fine)

---

## 🔐 Security Best Practices

### ✅ DO

- ✅ Use Streamlit Secrets for all credentials
- ✅ Keep credentials in a password manager
- ✅ Rotate API keys periodically
- ✅ Use different keys for dev and prod
- ✅ Monitor your Letta API usage

### ❌ DON'T

- ❌ Never commit secrets to Git
- ❌ Don't share secrets in screenshots
- ❌ Don't post secrets in support forums
- ❌ Don't use production keys for testing
- ❌ Don't share your deployment with untrusted users

---

## 📱 Screenshot Reference

When you're in Streamlit Cloud, you'll see:

```
┌─────────────────────────────────────────┐
│ Advanced settings                       │
├─────────────────────────────────────────┤
│ Python version                          │
│ [v] 3.12                                │
│                                         │
│ Secrets                                 │
│ Provide environment variables and       │
│ other secrets to your app using         │
│ TOML format...                          │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ LETTA_API_KEY = "lm-abc123"         │ │
│ │ LETTA_AGENT_ID = "agent-xxx..."     │ │
│ │ LETTA_PROJECT_ID = "proj-xxx"       │ │
│ │ LETTA_BASE_URL = "https://..."      │ │
│ │                                     │ │
│ │ APP_TITLE = "TalentScout..."        │ │
│ │ APP_ICON = "💼"                     │ │
│ │ DEBUG_MODE = false                  │ │
│ └─────────────────────────────────────┘ │
│                                         │
│               [Save]                    │
└─────────────────────────────────────────┘
```

---

## 🎉 Ready to Configure!

Now you know exactly what to paste in the Secrets section. 

### Quick Checklist

- [ ] Have your Letta credentials ready
- [ ] Open Streamlit app settings
- [ ] Go to Secrets section
- [ ] Paste the configuration (with your actual values)
- [ ] Save and wait 60 seconds
- [ ] Test your app

**Your configuration should look like this** (with your real values):

```toml
LETTA_API_KEY = "lm-your-key"
LETTA_AGENT_ID = "agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
LETTA_PROJECT_ID = "proj-your-project"
LETTA_BASE_URL = "https://api.letta.com"
APP_TITLE = "TalentScout AI Hiring Assistant"
APP_ICON = "💼"
DEBUG_MODE = false
```

---

**Need Help?** Check the [troubleshooting section](STREAMLIT_DEPLOYMENT_GUIDE.md#troubleshooting) in the deployment guide.
