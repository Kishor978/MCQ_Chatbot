
# Gemini Chatbot - MCQ Generator

This project is a Flask-based web application that generates multiple-choice questions (MCQs) using the Gemini API. The application allows users to input grade level, subject, and subtopic to generate relevant MCQs.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/MCQ_Chatbot.git
    cd MCQ_Chatbot
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the root directory.
    - Add your Google API key:
      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

## Usage

1. Run the Flask application:
    ```sh
    python [app.py]

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Fill in the form with the grade level, subject, and subtopic, then submit to generate MCQs.

## File Descriptions

- `app.py`: Main Flask application file.
- `MCQ_chatbot.py`: Additional chatbot functionalities.
- `prompt_template.txt`: Template file for generating prompts.
- `QnA_chatbot.py`: QnA chatbot functionalities.
- `requirements.txt`: List of required Python packages.
- `static/style.css`: CSS file for styling the web application.
- `templates/index.html`: HTML template for the web application.
- `utils/MCQ.py`: Utility functions for configuring the Gemini API, reading prompts, and getting responses.

## Functions

### `app.py`

- `home()`: Handles the homepage route, processes form submissions, and renders the template.

### `utils/MCQ.py`

- `configure_gemini_api()`: Configures the Gemini API using the provided API key.
- `get_gemini_response(model, question)`: Gets a response from the Gemini API.
- `read_prompt_from_file(grade, subject, subtopic, num_questions, filename='prompt_template.txt')`: Reads and formats the prompt from a file.
- `format_response_to_json(response_text)`: Converts the Gemini response to JSON format.

## Demo Video

Watch the demo video to see how the Gemini Chatbot - MCQ Generator works:


[![Watch the video](https://github.com/Kishor978/MCQ_Chatbot/blob/main/MCQ-genetator.mp4)](https://github.com/Kishor978/MCQ_Chatbot/blob/main/MCQ-genetator.mp4)