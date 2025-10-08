# 🎯 START HERE - Recruitment AI Agent

Welcome! You've just received a complete, production-ready Recruitment AI Agent application.

## ⚡ Quick Start (5 Minutes)

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Get Your API Key
Visit https://makersuite.google.com/app/apikey and get a free Gemini API key.

### 3️⃣ Configure
Create a file named `.env` with this content:
```
GEMINI_API_KEY=paste_your_key_here
```

**OR** run the automated setup:
```bash
python setup.py
```

### 4️⃣ Start the Server
```bash
uvicorn main:app --reload
```

### 5️⃣ Open Browser
Go to: http://localhost:8000

**That's it! You're ready to evaluate candidates! 🚀**

---

## 📚 Project Documentation

### For Quick Setup
- **HOW_TO_RUN.txt** - Command reference and troubleshooting
- **SETUP_GUIDE.md** - Step-by-step setup instructions

### For Understanding the Project
- **README.md** - Complete documentation (400+ lines)
- **PROJECT_OVERVIEW.md** - Technical architecture and details

### For Testing
- **test_files/** - Sample job description and resumes

---

## 📁 What's Included

### ✅ Backend Application
- `main.py` - Complete FastAPI application with all endpoints
- Full integration with Google Gemini AI
- PDF and DOCX file processing
- Automatic email generation

### ✅ Frontend Interface
- `templates/index.html` - Beautiful input form
- `templates/results.html` - Professional results display
- `static/styles.css` - Modern, responsive styling

### ✅ Configuration Files
- `requirements.txt` - All Python dependencies
- `.gitignore` - Git exclusion rules
- `setup.py` - Automated setup script

### ✅ Test Files
- Sample job description
- Sample resumes (strong and moderate candidates)
- Instructions for generating PDFs

### ✅ Documentation
- Complete README with setup, usage, and API docs
- Setup guide with troubleshooting
- Project overview with technical details
- Quick reference guide

---

## 🎨 Features

### Job Description Input (3 Methods)
1. **Paste Text** - Copy and paste your JD
2. **Upload File** - Upload PDF or DOCX
3. **Generate with AI** - Let AI create a JD for you

### Resume Evaluation
- Upload up to 10 resumes at once
- AI-powered scoring (0-100)
- Missing skills identification
- Personalized remarks for each candidate

### Email Generation
- Personalized interview invitation for top candidate
- Professional rejection email template
- One-click copy to clipboard

### Beautiful Interface
- Modern gradient design
- Responsive layout (works on all devices)
- Visual score indicators
- Color-coded results
- Summary statistics dashboard

---

## 🔧 Technology Stack

- **Backend**: Python 3.8+ with FastAPI
- **AI**: Google Gemini 1.5 Pro
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **File Processing**: pypdf, python-docx
- **Server**: Uvicorn ASGI server

---

## 📊 How It Works

```
1. User provides Job Description
   ↓
2. User uploads Resume files (PDF/DOCX)
   ↓
3. System extracts text from files
   ↓
4. AI analyzes each resume against JD
   ↓
5. System generates scores, missing skills, and remarks
   ↓
6. AI creates personalized emails
   ↓
7. Results displayed in beautiful interface
```

---

## 🎯 Perfect For

- HR professionals screening candidates
- Startup founders hiring their first team
- Recruitment agencies managing multiple clients
- Anyone who wants to save time on resume screening

---

## 💡 Quick Tips

### First Time Users
1. Start with the sample files in `test_files/`
2. Try the AI job description generator
3. Upload 2-3 resumes to see the scoring
4. Check out the auto-generated emails

### API Documentation
Once the server is running, visit:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

### Need Help?
- Check **SETUP_GUIDE.md** for detailed instructions
- See **README.md** for complete documentation
- Review **HOW_TO_RUN.txt** for quick commands

---

## ⚠️ Important Notes

1. **API Key Required**: You need a free Google Gemini API key
2. **API Costs**: Free tier is generous, but monitor your usage
3. **Processing Time**: 10 resumes take about 30-60 seconds
4. **Privacy**: Resume data is not stored by default

---

## 🚀 Next Steps After Setup

1. **Test with samples**: Use the provided test files
2. **Try your own**: Upload real resumes to evaluate
3. **Customize**: Modify prompts in `main.py` to suit your needs
4. **Deploy**: Consider deploying to a cloud platform
5. **Extend**: Add features like database storage or email integration

---

## 📈 Project Statistics

- **Total Files**: 15+ files
- **Lines of Code**: 1,500+ lines
- **Documentation**: 1,500+ lines
- **Features**: 10+ major features
- **API Endpoints**: 5 endpoints
- **Test Files**: 3 sample documents

---

## ✨ What Makes This Special

✓ **Complete Solution** - Everything you need is included  
✓ **Production Ready** - Can be deployed immediately  
✓ **Well Documented** - Comprehensive guides and comments  
✓ **Modern Stack** - Latest technologies and best practices  
✓ **AI Powered** - Leverages Google's Gemini for intelligence  
✓ **Beautiful UI** - Professional, responsive design  
✓ **Easy Setup** - Running in under 5 minutes  
✓ **Extensible** - Easy to customize and extend  

---

## 🎓 Learning Opportunities

This project demonstrates:
- FastAPI web application development
- AI/LLM integration (Gemini API)
- File processing (PDF/DOCX)
- Frontend development (HTML/CSS/JS)
- RESTful API design
- Prompt engineering
- Server-side rendering with Jinja2

---

## 📞 Support Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Gemini API Docs**: https://ai.google.dev/docs
- **Python Docs**: https://docs.python.org/

---

## 🎉 Ready to Start?

Run these commands:

```bash
# Install dependencies
pip install -r requirements.txt

# Run automated setup
python setup.py

# Edit .env file and add your API key

# Start the server
uvicorn main:app --reload

# Open browser to http://localhost:8000
```

---

**Built with ❤️ using Python, FastAPI, and Google Gemini AI**

**Time to revolutionize your recruitment process! 🚀**


