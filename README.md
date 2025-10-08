# 🤖 Recruitment AI Agent

A fully functional, AI-powered recruitment assistant built with Python and FastAPI. This application leverages the Google Gemini API to evaluate candidate resumes against job descriptions, providing match scores, missing skills analysis, and auto-generated personalized emails.

## 📋 Project Objective

Create an end-to-end recruitment solution that:
- Accepts job descriptions via multiple input methods (upload, paste, or AI-generation)
- Evaluates multiple candidate resumes simultaneously
- Provides intelligent matching scores and skill gap analysis
- Generates personalized interview invitation and rejection emails
- Presents results in an intuitive, professional interface

## ✨ Features

### Job Description Input (3 Methods)
1. **File Upload**: Upload JD as PDF or DOCX file
2. **Manual Text**: Paste job description directly
3. **AI Generation**: Generate JD using AI with custom parameters

### Resume Evaluation
- Upload up to 10 resumes (PDF or DOCX)
- AI-powered analysis using Google Gemini
- Match scoring (0-100 scale)
- Missing skills identification
- Personalized remarks for each candidate

### Email Generation
- Personalized interview invitation for top candidate
- Professional rejection email template
- Copy-to-clipboard functionality

### User Interface
- Clean, modern design with responsive layout
- Visual indicators for best matches
- Detailed evaluation tables
- Summary statistics dashboard

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, FastAPI
- **AI/LLM**: Google Gemini API (gemini-2.5-flash)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Templating**: Jinja2
- **File Processing**: pypdf (PDF), python-docx (DOCX)
- **Server**: Uvicorn ASGI server

## 📁 Project Structure

```
recruitment_agent/
│
├── static/
│   └── styles.css              # Frontend styling
│
├── templates/
│   ├── index.html              # Main input form page
│   └── results.html            # Evaluation results page
│
├── test_files/
│   ├── example_jd.docx         # Sample job description
│   ├── example_resume_1.pdf    # Sample resume 1
│   └── example_resume_2.pdf    # Sample resume 2
│
├── main.py                     # FastAPI application
├── requirements.txt            # Python dependencies
├── .env.template               # Environment variables template
├── .gitignore                  # Git ignore rules
├── setup.py                    # Setup script for test files
└── README.md                   # Project documentation
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- pip (Python package manager)

### Installation Steps

1. **Clone or download the repository**
   ```bash
   cd recruitment_agent
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root directory:
   ```bash
   # Windows
   copy .env.template .env

   # macOS/Linux
   cp .env.template .env
   ```

   Edit the `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

   **Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

5. **Generate test PDF files** (optional but recommended)
   ```bash
   python setup.py
   ```
   This will create PDF versions of the test files and set up your .env file.

6. **Verify setup**
   ```bash
   python main.py
   ```
   You should see output indicating the server is running.

## ▶️ How to Run the Project

### Start the development server

Using uvicorn directly (recommended):
```bash
uvicorn main:app --reload
```

Or using Python:
```bash
python main.py
```

### Access the application

Open your web browser and navigate to:
```
http://localhost:8000
```

### Interactive API documentation

FastAPI provides automatic interactive documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📖 How to Use

### Step 1: Provide Job Description

Choose one of three methods:

**Option A: Paste Text**
- Copy your job description
- Paste it into the text area

**Option B: Upload File**
- Click "Upload File" tab
- Select a PDF or DOCX file
- Click "Extract Text from File"

**Option C: Generate with AI**
- Click "Generate with AI" tab
- Fill in the form fields:
  - Job Title (e.g., "Senior Software Engineer")
  - Years of Experience (e.g., 5)
  - Must-Have Skills (comma-separated)
  - Company Name
  - Employment Type
  - Industry
  - Location
- Click "Generate Job Description"

### Step 2: Upload Resumes

- Click "Choose Files" under the resume upload section
- Select up to 10 resume files (PDF or DOCX)
- File count will update automatically

### Step 3: Evaluate Candidates

- Click "Evaluate Candidates" button
- Wait for AI analysis (may take 30-60 seconds for multiple resumes)
- View comprehensive results

### Step 4: Review Results

The results page displays:
- **Ranked candidate list** with scores and missing skills
- **Best match highlighted** with special badge
- **Interview invitation email** for top candidate
- **Rejection email template** for other candidates
- **Summary statistics** dashboard
- **Copy-to-clipboard** functionality for emails

## 🤖 AI Logic Explanation

### Resume Evaluation Process

1. **Text Extraction**: The application first extracts text content from uploaded PDF and DOCX files using specialized libraries (pypdf and python-docx).

2. **AI Analysis**: For each resume, the application sends a structured prompt to the Google Gemini API containing:
   - The complete job description
   - The extracted resume text
   - Instructions to evaluate the candidate

3. **Structured Response**: Gemini returns a JSON object for each candidate with:
   - `score`: Integer from 0-100 representing match quality
   - `missing_skills`: Array of skills from JD not found in resume
   - `remarks`: One-sentence explanation of the score

4. **Candidate Ranking**: Candidates are automatically ranked by their scores.

5. **Email Generation**: The application makes additional Gemini API calls to generate:
   - Personalized interview invitation for the best candidate
   - Professional rejection email template for other candidates

### Prompt Engineering

The application uses carefully crafted prompts that:
- Provide clear context about the evaluation task
- Request structured JSON output for reliable parsing
- Emphasize professional, objective evaluation criteria
- Generate empathetic, personalized communication

## 🎯 Model Choice: Why Google Gemini?

### Reasoning for Gemini Selection

**Google Gemini** was selected as the AI model for this application due to several key advantages:

1. **Strong Natural Language Understanding**
   - Gemini excels at comprehending complex job descriptions and resumes
   - Accurately identifies skills, experience levels, and qualifications
   - Understands context and nuance in professional documents

2. **Structured Output Capability**
   - Reliably generates valid JSON responses when properly prompted
   - Critical for the scoring system requiring consistent data format
   - Reduces parsing errors and improves application stability

3. **Complex Instruction Following**
   - Can follow multi-step evaluation instructions
   - Balances multiple criteria (skills, experience, culture fit)
   - Adapts evaluation style based on job requirements

4. **Content Generation Quality**
   - Produces professional, personalized emails
   - Maintains appropriate tone and empathy
   - Generates contextually relevant content

5. **API Accessibility**
   - Well-documented Python SDK (google-generativeai)
   - Straightforward authentication and configuration
   - Generous free tier for development and testing

6. **Cost-Effectiveness**
   - Competitive pricing for production use
   - Good balance of quality and cost
   - Suitable for real-world recruitment scenarios

### Alternative Considerations

While Gemini was chosen, other models like OpenAI's GPT-4, Anthropic's Claude, or open-source alternatives (Llama, Mistral) could also be viable depending on specific requirements around privacy, cost, or deployment constraints.

## 📂 Example Files

The `/test_files` directory contains sample files for testing:

- **example_jd.txt/.pdf**: Sample job description for a Senior Software Engineer role
- **example_resume_1.txt/.pdf**: Sample resume with strong match (7 years experience)
- **example_resume_2.txt/.pdf**: Sample resume with moderate match (3 years experience)

Use these files to test the application functionality without needing to prepare your own documents.

**Note**: Run `python setup.py` to automatically generate PDF versions of the text files for testing file upload functionality.

## 🔧 API Endpoints

### Frontend Routes
- `GET /` - Home page with input form
- `GET /health` - Health check endpoint

### API Routes
- `POST /generate-jd` - Generate job description with AI
  - Request body: JSON with job parameters
  - Returns: Generated JD text

- `POST /extract-jd` - Extract text from JD file
  - Request body: multipart/form-data with file
  - Returns: Extracted JD text

- `POST /evaluate` - Evaluate candidates
  - Request body: multipart/form-data with JD text and resume files
  - Returns: HTML results page

## 🔒 Security Considerations

- **API Key Protection**: API key stored in `.env` file (not in version control)
- **File Validation**: Only PDF and DOCX files accepted
- **Input Sanitization**: All user inputs processed safely
- **File Size Limits**: Enforced by FastAPI configuration
- **HTTPS**: Use HTTPS in production for secure data transmission

## 🐛 Troubleshooting

### Common Issues

**Issue**: "GEMINI_API_KEY environment variable is not set"
- **Solution**: Ensure `.env` file exists and contains valid API key

**Issue**: "Error extracting PDF/DOCX"
- **Solution**: Verify file is not corrupted and is a valid PDF/DOCX

**Issue**: "Failed to generate job description"
- **Solution**: Check internet connection and API key validity

**Issue**: Application won't start
- **Solution**: Verify all dependencies installed: `pip install -r requirements.txt`

## 📈 Future Enhancements

Potential improvements for future versions:
- Database integration for storing evaluations
- User authentication and multi-tenant support
- Batch processing for large recruitment campaigns
- Advanced analytics and reporting
- Integration with ATS (Applicant Tracking Systems)
- Resume parsing with structured data extraction
- Interview scheduling integration
- Candidate comparison visualizations

## 📄 License

This project is provided as-is for educational and commercial use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

For questions or support, please refer to the FastAPI and Google Gemini documentation:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)

---

**Built with ❤️ using FastAPI and Google Gemini AI**

