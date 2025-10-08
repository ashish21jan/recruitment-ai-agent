"""
Setup script for creating test PDF files from text files.
Run this script to generate PDF versions of test files for testing file upload functionality.
"""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    print("✓ reportlab is installed")
except ImportError:
    print("Installing reportlab for PDF generation...")
    import subprocess
    subprocess.check_call(["pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch

import os


def text_to_pdf(input_file, output_file):
    """Convert a text file to PDF format."""
    try:
        # Read the text file
        with open(input_file, 'r', encoding='utf-8') as f:
            text_content = f.read()
        
        # Create PDF
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Split text into paragraphs
        paragraphs = text_content.split('\n')
        
        for para in paragraphs:
            if para.strip():
                p = Paragraph(para.replace('<', '&lt;').replace('>', '&gt;'), styles['Normal'])
                story.append(p)
                story.append(Spacer(1, 0.1 * inch))
        
        # Build PDF
        doc.build(story)
        print(f"✓ Created: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Error creating {output_file}: {str(e)}")
        return False


def setup_test_files():
    """Create PDF versions of test files."""
    print("\n" + "="*60)
    print("Creating Test PDF Files")
    print("="*60 + "\n")
    
    test_files_dir = "test_files"
    
    # Ensure test_files directory exists
    if not os.path.exists(test_files_dir):
        os.makedirs(test_files_dir)
        print(f"Created directory: {test_files_dir}")
    
    # Define conversions
    conversions = [
        ("test_files/example_jd.txt", "test_files/example_jd.pdf"),
        ("test_files/example_resume_1.txt", "test_files/example_resume_1.pdf"),
        ("test_files/example_resume_2.txt", "test_files/example_resume_2.pdf"),
    ]
    
    success_count = 0
    for input_file, output_file in conversions:
        if os.path.exists(input_file):
            if text_to_pdf(input_file, output_file):
                success_count += 1
        else:
            print(f"✗ Source file not found: {input_file}")
    
    print(f"\n{'='*60}")
    print(f"Completed: {success_count}/{len(conversions)} files created successfully")
    print(f"{'='*60}\n")
    
    if success_count == len(conversions):
        print("✓ All test files are ready!")
        print("  You can now use the PDF files in test_files/ for testing the application.")
    else:
        print("⚠ Some files could not be created. Check the errors above.")


def create_env_file():
    """Create .env file from template if it doesn't exist."""
    if not os.path.exists('.env'):
        print("\n" + "="*60)
        print("Setting up .env file")
        print("="*60 + "\n")
        
        if os.path.exists('.env.template'):
            with open('.env.template', 'r') as template:
                content = template.read()
            
            with open('.env', 'w') as env_file:
                env_file.write(content)
            
            print("✓ Created .env file from template")
            print("⚠ IMPORTANT: Edit .env and add your GEMINI_API_KEY")
            print("  Get your API key from: https://makersuite.google.com/app/apikey")
        else:
            print("Creating .env file...")
            with open('.env', 'w') as env_file:
                env_file.write("# Google Gemini API Configuration\n")
                env_file.write("# Get your API key from: https://makersuite.google.com/app/apikey\n\n")
                env_file.write("GEMINI_API_KEY=your_gemini_api_key_here\n")
            
            print("✓ Created .env file")
            print("⚠ IMPORTANT: Edit .env and add your GEMINI_API_KEY")
    else:
        print("\n✓ .env file already exists")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 Recruitment AI Agent - Setup Script")
    print("="*60)
    
    # Create environment file
    create_env_file()
    
    # Create test PDFs
    setup_test_files()
    
    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Edit .env file and add your GEMINI_API_KEY")
    print("2. Run: uvicorn main:app --reload")
    print("3. Open: http://localhost:8000")
    print("\nHappy recruiting! 🤖\n")


