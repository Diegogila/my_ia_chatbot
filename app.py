from flask import Flask, request
import json
from flask_cors import CORS
from chatbot import to_talk

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']
    response = to_talk(input_text)
    return response

if __name__ == '__main__':
    app.run()
