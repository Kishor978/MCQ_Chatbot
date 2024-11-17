from flask import Flask, render_template, request
from utils import configure_gemini_api, get_gemini_response, read_prompt_from_file,format_response_to_json

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API and load the model
model = configure_gemini_api()

# Flask route for the homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        grade = request.form.get('grade')
        subject = request.form.get('subject')
        subtopic = request.form.get('subtopic')
        num_questions = request.form.get('num_questions')

        # Read the prompt from the text file
        prompt = read_prompt_from_file(grade, subject, subtopic, num_questions)


         # Get response from Gemini
        response_text = get_gemini_response(model, prompt)

        # Convert the response text to JSON format
        response_json = format_response_to_json(response_text)

        # Pass the JSON response to the template for rendering
        return render_template('index.html', mcq=response_json)

    return render_template('index.html', mcq=None)
if __name__ == '__main__':
    app.run(debug=True)
