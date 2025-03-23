from flask import Flask, request, render_template
import json
from flask_cors import CORS
from chatbot import to_talk

# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

@app.route('/', methods=['GET'])
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    """
    Handle the chatbot prompt sent via POST request.
    """
    # Get the data from the request
    data = request.get_data(as_text=True)
    # Parse the JSON data
    data = json.loads(data)
    # Extract the input text from the data
    input_text = data['prompt']
    # Get the response from the chatbot
    response = to_talk(input_text)
    # Return the response
    return response

if __name__ == '__main__':
    # Run the Flask application
    app.run()
