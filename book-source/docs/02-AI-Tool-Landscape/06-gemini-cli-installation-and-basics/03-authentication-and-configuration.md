---
sidebar_position: 3
title: Authentication & Configuration
---

# Authentication & Configuration

**Estimated time:** 15-20 minutes

## Why Authentication Matters

You've installed the Gemini CLI and verified your terminal environment. Before you can start coding with AI assistance, you need to **authenticate**—prove to Google's servers that you have permission to use the Gemini API.

Think of authentication like showing your library card before checking out books. The library (Google) needs to:
- **Verify your identity** (you are who you say you are)
- **Track your usage** (how many books/API requests you've borrowed)
- **Enforce limits** (free tier quotas)
- **Keep everyone's data secure** (your conversations stay private)

**Good news:** Authentication is a one-time setup that takes about 2 minutes. After this lesson, your CLI will "remember" your credentials.

---

## Understanding OAuth Authentication

The Gemini CLI uses **OAuth 2.0**, an industry-standard authentication protocol. Here's what that means in plain English:

**Traditional authentication** (username + password):
```
You → Send password → Google → Approve/Deny
```
❌ Problem: Your password is exposed to every app you use.

**OAuth authentication** (token-based):
```
You → Login via Google in browser → Google issues secure token → App uses token
```
✅ Benefit: Your password stays with Google. Apps get a temporary "access pass" instead.

**Why this matters:**
- **Security:** Even if the token is compromised, your Google account password is safe.
- **Granular control:** You can revoke CLI access without changing your password.
- **Automatic expiration:** Tokens expire after a time, requiring re-authentication.

### Three Authentication Methods

The Gemini CLI supports three authentication methods:

| Method | Best For | Setup Complexity |
|--------|----------|------------------|
| **Login with Google** | Beginners, personal projects | ⭐ Simple (1 command) |
| **API Key** | Automation, scripts | ⭐⭐ Moderate (manual key management) |
| **Vertex AI** | Enterprise, Google Cloud | ⭐⭐⭐ Advanced (Cloud project setup) |

**We'll focus on "Login with Google"** (Method 1) because it's the easiest and most secure for learning.

---

## Step-by-Step: Authenticate with Google Account

### Step 1: Start Authentication

Open your terminal and run:

```bash
gemini auth login
```

**Expected output:**

```
🔐 Opening browser for Google authentication...
🌐 Listening on http://localhost:8080 for OAuth callback...
```

**What's happening:**
1. The CLI starts a temporary local web server (on port 8080)
2. Your default browser opens to Google's login page
3. After you log in, Google redirects back to `localhost:8080`
4. The CLI captures the OAuth token and saves it

### Step 2: Complete Browser Login

**In your browser, you'll see:**

1. **Google Sign-In screen:**
   - Enter your Google account email
   - Enter your password

2. **Permission request:**
   ```
   "Gemini CLI" wants to:
   - View and manage your files in Google Drive
   - Access AI services on your behalf
   ```
   - Click **"Allow"**

3. **Success confirmation:**
   ```
   ✅ Authentication successful!
   You can close this window and return to your terminal.
   ```

### Step 3: Verify in Terminal

Back in your terminal, you should see:

```
✅ Authentication successful!
🔑 Token saved to: ~/.gemini/.auth/credentials.json
📊 Run 'gemini status' to view your quota.
```

**Congratulations!** You're now authenticated. The CLI has stored your OAuth token securely in your home directory.

---

## Verification: Check Your Status

Let's confirm everything works and see your API quota:

```bash
gemini status
```

**Expected output:**

```
🤖 Gemini CLI Status

Authentication:  ✅ Logged in as: your.email@gmail.com
Model:           gemini-2.0-flash-exp (default)
Region:          US (supported)

📊 API Quota (Free Tier):
   Rate Limit:   60 requests/minute
   Daily Limit:  1,000 requests/day
   Usage Today:  3 requests (0.3%)

🔗 Next Steps:
   - Try 'gemini chat' to start a conversation
   - Run 'gemini --help' for all commands
```

**Understanding this output:**

| Field | Meaning |
|-------|---------|
| **Authentication** | Confirms your Google account is linked |
| **Model** | Which AI model you're using (can be changed) |
| **Region** | Your geographic location (affects availability) |
| **Rate Limit** | Maximum 60 API calls per minute |
| **Daily Limit** | Maximum 1,000 API calls per day (resets at midnight UTC) |
| **Usage Today** | How many requests you've made so far |

---

## Understanding Free Tier Quotas

Google provides generous free quotas for learning and experimentation. Here's how to think about them:

### Rate Limit: 60 Requests/Minute

**What counts as a request:**
- Each message you send in `gemini chat`
- Each file you analyze with `gemini code review`
- Each command that contacts the API

**60 requests/minute is plenty for:**
- ✅ Interactive coding sessions (1-2 requests per minute)
- ✅ Testing and learning (even rapid experimentation)
- ❌ NOT for: Automated scripts running in tight loops

**What happens if you exceed:**
```
⚠️ Rate limit exceeded. Retrying in 10 seconds...
```
The CLI automatically waits and retries. You don't lose your request.

### Daily Limit: 1,000 Requests/Day

**How long does 1,000 requests last:**
- **Light usage** (learning, experimenting): Weeks without hitting the limit
- **Moderate usage** (daily coding sessions): 1-2 weeks
- **Heavy usage** (all-day coding): 2-3 days

**Example calculation:**
```
Average coding session: 2 hours
Requests per session: ~50-100 (asking questions, reviewing code)
Sessions per day: 2
Total per day: 100-200 requests
→ You'd need 5-10 days to hit 1,000
```

**What happens when you hit 1,000:**
```
❌ Daily quota exceeded. Resets at midnight UTC.
⏰ Time until reset: 14 hours, 23 minutes
```
Your quota resets every 24 hours (midnight UTC). Plan accordingly if you're approaching the limit.

### Monitoring Your Usage

Check your current usage anytime:

```bash
gemini status
```

**Pro tip:** If you're working on a long coding session, run `gemini status` periodically to see how many requests you have left.

---

## Basic Configuration

The Gemini CLI is highly customizable. Let's explore basic configuration options.

### Configuration File Location

Your settings are stored in:

```
~/.gemini/settings.json
```

**On Windows:**
```
C:\Users\YourName\.gemini\settings.json
```

**On macOS/Linux:**
```
/home/yourname/.gemini/settings.json
```

### Viewing Current Settings

```bash
gemini config list
```

**Example output:**

```json
{
  "model": "gemini-2.0-flash-exp",
  "theme": "auto",
  "vim_mode": false,
  "auto_save": true,
  "temperature": 0.7
}
```

### Common Customizations

**1. Change the AI model:**

```bash
gemini config set model gemini-1.5-pro
```

Available models:
- `gemini-2.0-flash-exp` (default, fastest, experimental)
- `gemini-1.5-pro` (slower, more accurate, stable)
- `gemini-1.5-flash` (balanced speed and quality)

**2. Enable Vim keybindings:**

```bash
gemini config set vim_mode true
```

**3. Change color theme:**

```bash
gemini config set theme dark
```

Options: `light`, `dark`, `auto` (follows system theme)

**4. Adjust AI creativity (temperature):**

```bash
gemini config set temperature 0.9
```

Temperature range: `0.0` (deterministic) to `1.0` (creative)
- **0.0-0.3:** Consistent, factual responses (best for code)
- **0.4-0.7:** Balanced (default)
- **0.8-1.0:** Creative, varied responses (best for brainstorming)

### Configuration via Environment Variables

You can also configure settings via environment variables (useful for temporary changes or scripts):

```bash
# Use a specific model for this session only
export GEMINI_MODEL="gemini-1.5-pro"

# Increase creativity
export GEMINI_TEMPERATURE="0.9"

# Run a command with custom settings
gemini chat "Suggest creative project names"
```

**Persistent environment variables:**

Add to your shell configuration file:

**On macOS/Linux (Bash):**
```bash
echo 'export GEMINI_MODEL="gemini-1.5-pro"' >> ~/.bashrc
source ~/.bashrc
```

**On macOS (Zsh):**
```bash
echo 'export GEMINI_MODEL="gemini-1.5-pro"' >> ~/.zshrc
source ~/.zshrc
```

**On Windows (PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable('GEMINI_MODEL', 'gemini-1.5-pro', 'User')
```

### Configuration Hierarchy

When the CLI looks for settings, it checks in this order:

1. **Command-line flags** (highest priority)
   ```bash
   gemini chat --model gemini-1.5-pro "Hello"
   ```

2. **Environment variables**
   ```bash
   export GEMINI_MODEL="gemini-1.5-pro"
   ```

3. **Configuration file** (`~/.gemini/settings.json`)

4. **Built-in defaults** (lowest priority)

**Why this matters:** You can override settings temporarily without changing your config file.

---

## Special Cases: Alternative Authentication Methods

### Google Workspace Accounts

If you're using a **Google Workspace account** (e.g., `you@company.com`), you may need to set up a Google Cloud project:

**Why this is required:**
- Workspace admins control API access
- Your organization may have specific billing/quota policies

**Setup steps:**

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project: `my-gemini-cli`
3. Enable the Gemini API for your project
4. Note your project ID (e.g., `my-gemini-cli-123456`)

5. Set the environment variable:
   ```bash
   export GOOGLE_CLOUD_PROJECT="my-gemini-cli-123456"
   ```

6. Re-authenticate:
   ```bash
   gemini auth login
   ```

**Persist the project ID:**

```bash
echo 'export GOOGLE_CLOUD_PROJECT="my-gemini-cli-123456"' >> ~/.bashrc
source ~/.bashrc
```

### Regional Restrictions

The Gemini API is not available in all countries. If you see:

```
❌ Error: Gemini API is not available in your region.
```

**Your options:**

1. **Use a VPN** to connect from a supported region (US, UK, most of EU)
   - ⚠️ Check Google's Terms of Service first

2. **Use Qwen Code as an alternative** (see below)

### Alternative: Qwen Code CLI (2,000 req/day)

If Gemini is unavailable in your region, **Qwen Code** is a strong alternative with higher quotas:

**Install Qwen CLI:**

```bash
npm install -g @qwencode/cli
```

**Authenticate:**

```bash
qwen auth login
```

**Quota comparison:**

| Feature | Gemini CLI | Qwen Code |
|---------|-----------|-----------|
| Free tier requests/day | 1,000 | 2,000 |
| Rate limit | 60/min | 100/min |
| Regional restrictions | Some regions blocked | Globally available |
| Model quality | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**Usage is nearly identical:**

```bash
# Gemini
gemini chat "Explain async/await"

# Qwen
qwen chat "Explain async/await"
```

---

## Troubleshooting Common Issues

### Issue 1: Browser Doesn't Open

**Problem:**
```
🔐 Opening browser for Google authentication...
❌ Error: Could not open browser.
```

**Causes:**
- No GUI environment (SSH session, headless server)
- Browser not in system PATH

**Solutions:**

**Option A: Copy authentication URL manually**

```bash
gemini auth login --no-browser
```

Output:
```
🔗 Copy this URL into your browser:
https://accounts.google.com/o/oauth2/v2/auth?client_id=...

Then paste the authorization code here:
```

1. Copy the URL
2. Paste into any browser (even on another device)
3. Complete login
4. Copy the authorization code from the redirect URL
5. Paste back into terminal

**Option B: Use API key instead**

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
gemini status
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

⚠️ **Security warning:** API keys are like passwords. Never commit them to Git or share publicly.

---

### Issue 2: Authentication Fails

**Problem:**
```
❌ Authentication failed: invalid_grant
```

**Causes:**
- Token expired
- Account permissions changed
- Clock skew (system time incorrect)

**Solutions:**

**Clear existing credentials:**

```bash
rm -rf ~/.gemini/.auth
gemini auth login
```

**Check system time:**

```bash
date
```

If your system time is wrong (more than 5 minutes off), sync it:

**On macOS/Linux:**
```bash
sudo ntpdate -s time.nist.gov
```

**On Windows (PowerShell as admin):**
```powershell
w32tm /resync
```

---

### Issue 3: Network/Proxy Issues

**Problem:**
```
❌ Error: connect ETIMEDOUT
```

**Causes:**
- Firewall blocking localhost:8080
- Corporate proxy intercepting OAuth redirect
- VPN interfering with localhost

**Solutions:**

**Option 1: Use a different port**

```bash
gemini auth login --port 9090
```

**Option 2: Configure proxy settings**

```bash
export HTTP_PROXY="http://proxy.company.com:8080"
export HTTPS_PROXY="https://proxy.company.com:8080"
gemini auth login
```

**Option 3: Disable VPN temporarily**

Some VPNs block localhost connections. Try disconnecting during authentication.

---

### Issue 4: Google Account Problems

**Problem:**
```
❌ This Google Account cannot access the Gemini API.
```

**Causes:**
- Account under 18 years old
- Account region restricted
- Terms of Service not accepted

**Solutions:**

**For users under 18:**
- Use a parent/guardian's account
- Or set up a Google Cloud project with billing (requires adult supervision)

**For region restrictions:**
- See "Regional Restrictions" section above
- Consider Qwen Code alternative

**Accept Terms of Service:**
1. Go to [Google AI Studio](https://makersuite.google.com)
2. Click "Get API Key"
3. Read and accept Terms of Service
4. Try `gemini auth login` again

---

### Issue 5: Regional Access Errors

**Problem:**
```
❌ The Gemini API is not available in your region.
```

**Cause:**
Google restricts API access in some countries for compliance reasons.

**Solutions:**

**Option 1: Check supported regions**

```bash
gemini regions list
```

Supported regions (as of 2024):
- ✅ United States, Canada
- ✅ United Kingdom, most EU countries
- ✅ Australia, New Zealand
- ✅ Japan, South Korea, Singapore
- ❌ China, Russia, Iran (blocked)

**Option 2: Use VPN**

Connect to a supported region via VPN, then authenticate.

⚠️ **Important:** Check Google's Terms of Service regarding VPN use.

**Option 3: Switch to Qwen Code**

Qwen Code is globally available (see "Alternative: Qwen Code CLI" section).

---

### Issue 6: Token Expiration

**Problem:**
```
⚠️ Your authentication token has expired.
🔐 Please run 'gemini auth login' to re-authenticate.
```

**Cause:**
OAuth tokens expire after 7 days of inactivity for security.

**Solution:**

Simply re-authenticate:

```bash
gemini auth login
```

**Pro tip:** If you use the CLI daily, tokens auto-refresh and never expire.

---

## Practice Exercises

### Exercise 1: Complete Authentication (Required)

**Task:** Authenticate with your Google account and verify status.

**Steps:**
1. Run `gemini auth login`
2. Complete browser login
3. Run `gemini status` to verify
4. Take a screenshot of your status output

**Success criteria:**
- ✅ Status shows "Logged in as: your.email@gmail.com"
- ✅ Quota displays "60 requests/minute" and "1,000 requests/day"
- ✅ No error messages

---

### Exercise 2: Check Your Quota

**Task:** Monitor your quota usage.

**Steps:**
1. Run `gemini status` and note your current usage
2. Run `gemini chat "Hello, Gemini!"`
3. Run `gemini status` again

**Questions:**
- How many requests did you use in step 2?
- How many requests do you have left today?
- At what time will your quota reset?

**Expected:**
- Usage should increase by 1 request
- Reset time is midnight UTC

---

### Exercise 3: Customize One Setting (Optional)

**Task:** Change your CLI theme to match your preference.

**Steps:**
1. Run `gemini config list` to see current theme
2. Change to dark mode: `gemini config set theme dark`
3. Open `gemini chat` and observe the new color scheme
4. (Optional) Change back to your preferred theme

**Bonus challenge:**
- Try changing the model to `gemini-1.5-pro`
- Ask a complex coding question and compare response quality

---

## Key Takeaways

🎯 **What you learned:**

1. **Authentication is one-time setup** using OAuth for security
2. **Free tier quotas are generous** (60/min, 1,000/day)
3. **Configuration is flexible** (file, env vars, command flags)
4. **Troubleshooting follows a pattern** (check auth → check network → check region)
5. **Alternatives exist** (API keys, Qwen Code, Vertex AI)

🔐 **Security best practices:**
- Never commit API keys to version control
- Store credentials in `~/.gemini/.auth/` (ignored by Git)
- Revoke access if a device is lost or compromised

📊 **Quota management:**
- Run `gemini status` to monitor usage
- Rate limit (60/min) auto-retries (no action needed)
- Daily limit (1,000/day) resets at midnight UTC

---

## What's Next?

**You're now authenticated and configured!** 🎉

In **Lesson 4: Your First AI-Powered Commands**, we'll:
- Start your first conversation with `gemini chat`
- Ask Gemini to explain code concepts
- Use `gemini code review` to analyze files
- Explore interactive commands

**Preview challenge:** Think of a Python concept you've always found confusing. In the next lesson, you'll ask Gemini to explain it in simple terms. Write it down now:

```
My confusing concept: ___________________________________
```

---

## Additional Resources

- **Google AI Studio:** [makersuite.google.com](https://makersuite.google.com) (get API keys, test models)
- **OAuth 2.0 Explained:** [oauth.net](https://oauth.net/2/) (deep dive into authentication)
- **Gemini API Quotas:** [Official documentation](https://ai.google.dev/pricing) (up-to-date limits)
- **Qwen Code CLI:** [qwencode.com/cli](https://qwencode.com/cli) (alternative for restricted regions)

**Need help?**
- Community forum: [community.google.com/ai](https://community.google.com/ai)
- GitHub issues: [github.com/google/gemini-cli](https://github.com/google/gemini-cli)
- Stack Overflow: Tag `gemini-api` or `gemini-cli`

---

## Lesson Complete! ✅

You've successfully:
- ✅ Authenticated with your Google account
- ✅ Verified your API quota
- ✅ Configured basic settings
- ✅ Learned troubleshooting strategies

**Ready to start coding with AI?** Move on to **Lesson 4** to send your first commands! 🚀
