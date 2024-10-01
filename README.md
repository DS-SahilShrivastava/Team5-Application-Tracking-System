# Team 5 - Application Tracking System (ATS)

This project is an **Applicant Tracking System (ATS)** that assists users in evaluating their resumes against a job description. It leverages the **OpenAI GPT model** to assess resumes by comparing them to job descriptions, providing a percentage match, identifying relevant keywords, and offering tailored recommendations for improvement. This project is developed using **Streamlit** for a user-friendly interface.

## Features

- **PDF Resume Upload**: Users can upload their resume in PDF format for analysis.
- **Job Description Matching**: The application compares the uploaded resume with a job description (optional) and calculates a percentage match.
- **Keyword Matching**: Identifies matching and missing keywords between the resume and job description.
- **Detailed Analysis**: Provides a detailed breakdown of resume content, including missing keywords and a percentage match score.
- **Recommendations for Improvement**: Tailored suggestions to improve the resume’s match with the job description.
- **Lottie Animations**: Provides an engaging user experience through Lottie animations.
  
## How It Works

1. **Upload Resume**: Users can upload their resume in PDF format through the interface.
2. **Input Job Description**: Users may provide a job description to compare the resume against. This step is optional.
3. **Analyze Resume**: Once the resume is uploaded and submitted, the system processes the resume using the OpenAI GPT model, returning:
   - Percentage match between the resume and job description.
   - List of matching keywords from the resume and job description.
   - List of missing keywords.
   - Profile summary.
   - Suggestions for improvement.
4. **Result Display**: The result is shown on the screen in an easy-to-read format with visual indicators for success or errors.

## Application

The **Team 5 ATS** is suitable for anyone looking to:
- **Improve their resume** by aligning it better with job descriptions.
- **Job seekers** who want to optimize their applications for specific roles in competitive industries like software engineering, data science, data analytics, and big data engineering.
- **Recruiters or hiring managers** who want to quickly assess the fit of a candidate's resume with a job description.

## Installation

Follow the steps below to run this project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/DS-SahilShrivastava/Team5-Application-Tracking-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Team5-Application-Tracking-System
```
### 3.Install Dependencies
Before running the application, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 4.Set Up Environment Variables
The application uses Azure OpenAI  to generate responses. Ensure you have the following environment variables set in your system or a .env file:

AZURE_OPENAI_API_KEY: Your Azure OpenAI API key.
AZURE_OPENAI_API_BASE: Your Azure OpenAI endpoint.
AZURE_OPENAI_API_VERSION: The version of the Azure OpenAI API to use (e.g., 2023-08-01-preview).
You can create a .env file in the project root and add your API credentials like so:

```bash
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_API_BASE=https://your_openai_endpoint
AZURE_OPENAI_API_VERSION=2023-08-01-preview
```

### 5.Run the Application
After setting up your environment variables and installing dependencies, run the Streamlit app:

```bash
streamlit run app.py
```

### 6.Access the Application
Once the application is running, it will be available at http://localhost:8501 in your web browser. From there, you can upload resumes and job descriptions for analysis.

