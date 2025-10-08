# 🚀 Quick Setup Guide

This guide will help you get the Recruitment AI Agent up and running in minutes.

## Prerequisites

- Python 3.8 or higher installed
- Google Gemini API key ([Get one for free](https://makersuite.google.com/app/apikey))

## Setup Steps

### 1. Install Python Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

This will install all required packages including FastAPI, Uvicorn, Google Generative AI, and file processing libraries.

### 2. Configure API Key

You need a Google Gemini API key to run this application.

#### Get Your API Key:
1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

#### Create .env File:

**Option A - Automatic (Recommended):**
```bash
python setup.py
```
Then edit the created `.env` file and replace `your_gemini_api_key_here` with your actual key.

**Option B - Manual:**

Create a new file named `.env` in the project root directory with the following content:
```
GEMINI_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with the API key you copied.

### 3. Generate Test Files (Optional)

To create PDF test files for easy testing:

```bash
python setup.py
```

This creates PDF versions of the sample job description and resumes in the `test_files/` directory.

### 4. Start the Application

Run the server:

```bash
uvicorn main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 5. Access the Application

Open your web browser and navigate to:

```
http://localhost:8000
```

You should see the Recruitment AI Agent home page!

## Testing the Application

### Quick Test with Sample Files:

1. **Provide Job Description:**
   - Copy the content from `test_files/example_jd.txt`
   - Paste it into the "Job Description Text" area
   - OR click "Upload File" and upload `test_files/example_jd.pdf` (if you ran setup.py)

2. **Upload Resumes:**
   - Click "Choose Files" under "Upload Resumes"
   - Select both `example_resume_1.pdf` and `example_resume_2.pdf` from the `test_files/` folder
   - OR you can create your own PDF resumes

3. **Evaluate:**
   - Click "Evaluate Candidates"
   - Wait 30-60 seconds for AI analysis
   - View comprehensive results with scores, missing skills, and generated emails

### Test AI Job Description Generation:

1. Click the "Generate with AI" tab
2. Fill in the form:
   - Job Title: `Senior Python Developer`
   - Years of Experience: `5`
   - Skills: `Python, FastAPI, AWS, Docker`
   - Company Name: `Your Company`
   - Employment Type: `Full-time`
   - Industry: `Technology`
   - Location: `Remote`
3. Click "Generate Job Description"
4. The AI will create a complete job description for you!

## Troubleshooting

### Error: "GEMINI_API_KEY environment variable is not set"

**Solution:** 
- Make sure you created the `.env` file
- Verify the API key is correctly pasted (no extra spaces)
- Restart the server after creating/editing `.env`

### Error: "Error extracting PDF"

**Solution:**
- Ensure the file is a valid PDF or DOCX
- Try with the provided test files first
- Check that pypdf and python-docx are installed

### Server won't start

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check Python version
python --version  # Should be 3.8+

# Try running directly
python main.py
```

### Port already in use

**Solution:**
```bash
# Use a different port
uvicorn main:app --reload --port 8001

# Then access at http://localhost:8001
```

## API Documentation

Once the server is running, you can access interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These interfaces let you test API endpoints directly from your browser.

## Project Structure Quick Reference

```
recruitment_agent/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Your API key (create this!)
├── .env.template        # Template for .env file
├── setup.py            # Setup script
├── static/
│   └── styles.css      # Frontend styling
├── templates/
│   ├── index.html      # Input form page
│   └── results.html    # Results page
└── test_files/
    ├── example_jd.txt/pdf
    ├── example_resume_1.txt/pdf
    └── example_resume_2.txt/pdf
```

## Next Steps

Once everything is working:

1. **Customize**: Modify the prompts in `main.py` to adjust how the AI evaluates candidates
2. **Extend**: Add new features like database storage, user authentication, or email integration
3. **Deploy**: Consider deploying to a cloud platform (Heroku, AWS, Google Cloud)
4. **Scale**: Add caching, background tasks, or database for production use

## Getting Help

- Check the main [README.md](README.md) for detailed documentation
- Review the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Consult the [Google Gemini API docs](https://ai.google.dev/docs)

## Important Notes

- **API Costs**: The Gemini API has a free tier, but check usage limits
- **Privacy**: Be careful with sensitive resume data in production
- **Security**: Never commit your `.env` file to version control
- **Performance**: Processing multiple resumes takes time; be patient

---

**You're all set! Happy recruiting with AI! 🤖**


