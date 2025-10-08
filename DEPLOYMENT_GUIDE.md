# 🚀 Deployment Guide - Render

This guide will help you deploy your Recruitment AI Agent to Render for **FREE** and get a public URL.

## 📋 Prerequisites

1. A GitHub account (to host your code)
2. A Render account (free - sign up at https://render.com)
3. Your Gemini API key

---

## 🔧 Step 1: Push Your Code to GitHub

### Option A: Using Git Command Line

1. **Initialize Git repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Recruitment AI Agent"
   ```

2. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it: `recruitment-ai-agent`
   - Keep it Public or Private (both work with Render)
   - Don't initialize with README (you already have one)
   - Click "Create repository"

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/recruitment-ai-agent.git
   git branch -M main
   git push -u origin main
   ```

### Option B: Using GitHub Desktop

1. Open GitHub Desktop
2. Add this folder as a repository
3. Commit all files
4. Publish to GitHub

---

## 🌐 Step 2: Deploy to Render

### A. Sign Up/Login to Render

1. Go to https://render.com
2. Click "Get Started" or "Sign In"
3. Sign up with GitHub (recommended)

### B. Create New Web Service

1. Click "**New +**" button (top right)
2. Select "**Web Service**"

### C. Connect Your GitHub Repository

1. Click "**Connect a repository**"
2. Grant Render access to your GitHub repositories
3. Find and select your `recruitment-ai-agent` repository
4. Click "**Connect**"

### D. Configure Your Web Service

Fill in the following settings:

| Field | Value |
|-------|-------|
| **Name** | `recruitment-ai-agent` (or any name you prefer) |
| **Region** | Select closest to you (e.g., Oregon) |
| **Branch** | `main` |
| **Root Directory** | Leave blank |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Plan** | **Free** ⭐ |

### E. Add Environment Variable

**CRITICAL STEP:**

1. Scroll down to "**Environment Variables**"
2. Click "**Add Environment Variable**"
3. Add:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your actual Gemini API key
4. Click "**Add**"

### F. Deploy!

1. Scroll to the bottom
2. Click "**Create Web Service**"
3. Wait 5-10 minutes for deployment (first time)

---

## ✅ Step 3: Get Your Application URL

Once deployment is complete:

1. Your app URL will be shown at the top: `https://your-service-name.onrender.com`
2. Click the URL to open your application
3. **Done!** Your Recruitment AI Agent is live! 🎉

---

## 🔍 Example URL

Your URL will look like:
```
https://recruitment-ai-agent-abcd.onrender.com
```

---

## ⚠️ Important Notes

### Free Tier Limitations

1. **Automatic Sleep**: Free services sleep after 15 minutes of inactivity
   - First request after sleep takes ~30-60 seconds to wake up
   - Subsequent requests are fast

2. **Monthly Limits**:
   - 750 hours/month (enough for continuous use)
   - Free tier instances spin down after inactivity

3. **No Custom Domain**: Free tier uses Render's subdomain
   - Upgrade to paid plan for custom domains

### Keep Your Service Active

To prevent sleeping, you can:
- Use a service like **UptimeRobot** (free) to ping your URL every 15 minutes
- Upgrade to a paid plan ($7/month) for always-on service

---

## 🔧 Troubleshooting

### Build Failed

**Check**:
- All files are committed to GitHub
- `requirements.txt` is present
- Build command is correct

**Solution**: Check the build logs in Render dashboard

### Service Starts But Won't Load

**Check**:
- Environment variable `GEMINI_API_KEY` is set correctly
- Start command uses `--host 0.0.0.0 --port $PORT`
- No syntax errors in `main.py`

**Solution**: Check the service logs in Render dashboard

### API Key Error

**Check**:
- Environment variable name is exactly `GEMINI_API_KEY`
- API key is valid and not revoked
- No extra spaces in the value

**Solution**: Update the environment variable in Render settings

### Static Files Not Loading

**Check**:
- `static/` and `templates/` folders are in the repository
- Paths in `main.py` are correct

**Solution**: Verify folders are committed to GitHub

---

## 📊 Monitoring Your Deployment

### View Logs

1. Go to your service dashboard on Render
2. Click "**Logs**" tab
3. See real-time logs of your application

### Check Health

Visit: `https://your-service-name.onrender.com/health`

Should return:
```json
{
  "status": "healthy",
  "message": "Recruitment AI Agent is running"
}
```

### View Metrics

1. Go to "**Metrics**" tab
2. See CPU, Memory, and Request statistics

---

## 🔄 Updating Your Application

Every time you push changes to GitHub:

1. Commit your changes locally:
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```

2. Render automatically detects changes and redeploys
3. Check deployment status in Render dashboard

---

## 💰 Cost Analysis

### Free Tier (Current Setup)
- **Cost**: $0/month
- **Limitations**: Sleeps after 15 min inactivity
- **Best For**: Testing, demos, low-traffic use

### Paid Tier (Optional Upgrade)
- **Cost**: $7/month
- **Benefits**: 
  - Always-on (no sleeping)
  - Custom domains
  - More resources
  - Priority support

---

## 🎯 Alternative Free Hosting Options

If Render doesn't work, try:

1. **Railway** (https://railway.app)
   - $5 free credit/month
   - Similar deployment process

2. **Fly.io** (https://fly.io)
   - Free tier available
   - More configuration required

3. **Heroku** (https://heroku.com)
   - Free tier discontinued, but $5/month available

---

## 📱 Share Your Application

Once deployed, share your URL:
```
https://your-service-name.onrender.com
```

Users can:
- ✅ Upload job descriptions
- ✅ Evaluate resumes
- ✅ Generate AI-powered emails
- ✅ No installation required!

---

## 🔐 Security Reminder

- ✅ Never commit your `.env` file (already in `.gitignore`)
- ✅ Always use Environment Variables on Render
- ✅ Keep your Gemini API key secret
- ✅ Monitor your API usage on Google Cloud Console

---

## 🆘 Need Help?

- **Render Documentation**: https://render.com/docs
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Render Community**: https://community.render.com

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Repository connected to Render
- [ ] Build command configured
- [ ] Start command configured
- [ ] `GEMINI_API_KEY` environment variable added
- [ ] Service deployed successfully
- [ ] Health check passes
- [ ] Application accessible via URL

---

**Your Recruitment AI Agent is now live on the internet! 🌐🎉**

