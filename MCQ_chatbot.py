import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# loading Gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    try:
        response=model.generate_content(question)
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Chatbot")

# Collect user input for the MCQ generation
grade = st.text_input("Enter the grade level (e.g., 5th grade):", "5th grade")
subject = st.text_input("Enter the subject (e.g., Mathematics):", "Mathematics")
subtopic = st.text_input("Enter the subtopic (e.g., Algebra):", "Algebra")
num_questions = st.number_input("Enter the number of questions (e.g., 5):", min_value=1, max_value=10, value=5)

submit=st.button("Generate MCQs")

if submit:
    prompt = f"""
    Create {num_questions} multiple-choice questions for a {grade} grade student on the subject of {subject}.
    The subtopic is {subtopic}. Each question should have 4 options, with one correct answer.
    """
    response=get_gemini_response(prompt)
    if response:
        st.subheader("Generated MCQs:")
        st.write(response)
    else:
        st.write("No response received. Check the input or API key.")



