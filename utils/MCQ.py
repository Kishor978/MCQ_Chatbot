import os
import google.generativeai as genai
import json

# Function to configure the Gemini API
def configure_gemini_api():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-pro")

# Function to get Gemini response
def get_gemini_response(model, question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to read and format prompt from file
def read_prompt_from_file(grade, subject, subtopic, num_questions, filename='prompt_template.txt'):
    try:
        with open(filename, 'r') as file:
            template = file.read()
            # Replace placeholders with actual values
            prompt = template.format(
                grade=grade, 
                subject=subject, 
                subtopic=subtopic, 
                num_questions=num_questions
            )
        return prompt
    except Exception as e:
        return f"Error reading file: {str(e)}"
 
# Function to convert Gemini response to JSON structure
def format_response_to_json(response_text):
    # You might want to improve this if the response is not cleanly structured
    try:
        # Split the response text into questions based on some separator (adjust as needed)
        questions = response_text.split("\n\n")  # Assuming each question is separated by double newlines
        json_data = {"questions": []}

        for question in questions:
            # Split question into the main question and the answers
            parts = question.split("\n")
            if len(parts) >= 5:  # Expect at least 1 question + 4 options
                question_text = parts[0]
                options = parts[1:5]  # First 4 lines after the question are options
                correct_answer = options[0]  # Assume the first option is the correct one (adjust logic)
                
                json_data["questions"].append({
                    "question": question_text,
                    "options": options,
                    "correct_answer": correct_answer
                })
        
        return json.dumps(json_data, indent=4)  # Return formatted JSON
    except Exception as e:
        return f"Error formatting to JSON: {str(e)}"