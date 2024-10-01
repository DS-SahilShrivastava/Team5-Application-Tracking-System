import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
import openai
import os
from streamlit_lottie import st_lottie
import requests

# Load environment variables
load_dotenv()

# Function to get the response from OpenAI GPT model
def get_openai_response(input_text):

    try:
        # Define the API key and client setup for Azure OpenAI
        openai.api_type = "azure"
        openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")  # Store your key in environment variables for security
        openai.api_base = "https://ai-proxy.lab.epam.com"  # Your Azure OpenAI endpoint
        openai.api_version = "2023-08-01-preview"

        # Loop through deployments and make the API call
        for deployment in ['gpt-4', 'Mixtral-8x7B-Instruct-v0.1', 'gpt-35-turbo-0613', 'amazon.titan-tg1-large']:
            print(deployment)

            # Create a chat completion request
            response = openai.ChatCompletion.create(
                engine=deployment,
                temperature=0,
                messages=[
                    {"role": "system", "content": "You are a skilled ATS with deep knowledge in the tech field."},
                    {"role": "user", "content": input_text}
                ],
                max_tokens=1500
            )

            # Print the response
            print(response)
            return response['choices'][0]['message']['content']

    except Exception as e:
        return f"Error: {str(e)}"

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Function to load Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations
lottie_resume = load_lottieurl("https://lottie.host/051d1d7f-88a6-4d3d-ab05-835dae68bb2e/ybg6nMTWBA.json")
lottie_loading = load_lottieurl("https://lottie.host/786b84d8-137f-4f09-846a-912304bc5a92/brYR7E0UKM.json")

# The input prompt for OpenAI API
input_prompt = """
Act as an expert-level ATS (Applicant Tracking System) with a strong grasp of technical fields such as software engineering, data science, data analytics, and big data engineering. Your role is to critically assess the provided resume based on the job description (JD), considering that the job market is highly competitive. You must accurately assign a percentage match between the resume and JD, paying close attention to missing and matching keywords that are crucial for success in the role.

The evaluation should include:
1. **Percentage Match** (bolded).IF THE PERCENTAGE IS ABOVE 85% YOU CAN GIVE AN OUTPUT AS ACCEPTED OR REJECTED
2. A list of **matching keywords** found in the resume that align with the job description.
3. A concise, point-form list of **missing keywords** (bolded for emphasis) based on the JD.
4. Space for the candidate's **profile summary** as listed in the resume.

End with actionable, specific recommendations for improvement, tailored to increase the resume’s match with the job description.

Input: 
Resume Text: {text}
Job Description: {jd}

"""

# Streamlit App Design
st.set_page_config(page_title="Resume Tracker", page_icon=":clipboard:", layout="wide")

# Sidebar: Job Description and Resume Upload
st.sidebar.title("📄 Team 5 Resume Tracking System")
st.sidebar.markdown("**Improve Your Resume Right Now!**")
jd = st.sidebar.text_area("📝 Paste the Job Description",
                          placeholder="Input the Job description for matching, or leave empty for profile review and recommendations.")
uploaded_file = st.sidebar.file_uploader("📂 Upload Your Resume", type="pdf", help="Please upload the resume in PDF format.")
submit = st.sidebar.button("🚀 Submit")

# Lottie animation in the main content
st_lottie(lottie_resume, height=300, key="resume_animation")

# Default homepage content
if uploaded_file is None:
    st.title("Welcome to the Team 5 Resume Tracking System")
    st.markdown("---")
    st.markdown("""
        ### 🛠️ How it works:
        1. Upload your resume in PDF format.
        2. Provide a job description (optional).
        3. Get detailed analysis on keyword matching, missing skills, and receive recommendations to improve your resume.
    """)
    st.markdown("---")
    st.info('💡 Tip: Make sure your resume is well-structured for better results.')
    st.warning('⚠️ Please upload resumes in .pdf format only.')

# Process submission when resume is uploaded and user clicks submit
if submit:
    if uploaded_file is not None:
        # Show loading animation while processing
        with st.spinner("Analyzing your resume... Please wait"):
            st_lottie(lottie_loading, height=150, key="loading")

            # Extract the text from the uploaded PDF
            resume_text = input_pdf_text(uploaded_file)
            space = "                                                      "

            # Generate the full input prompt for the AI
            full_input = f"resume: {resume_text} as resume information {space}job description: {jd} {space}{input_prompt}"

            # Get the AI-generated response
            response = get_openai_response(full_input)

        # Display the response in a more organized way
        st.subheader("📊 Resume Analysis Result")
        st.markdown(f"**Job Description Matching Percentage**: {response}")
        st.success("✅ Analysis completed successfully!")
    else:
        st.error("❌ Please upload a resume before submitting.")

# Footer
st.markdown("---")
st.markdown("🧑‍💻 Created by [Team 5 @GEN AI KATA]")
