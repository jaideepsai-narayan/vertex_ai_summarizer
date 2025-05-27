from flask import Flask, request, jsonify
from flask_cors import CORS
from web import out,rag_qa  # This handles the URL processing

app = Flask(__name__)
CORS(app)  # Enable CORS for local development

@app.route('/process-url', methods=['POST'])
def process_url():
    data = request.get_json()
    url = data.get('url', '').strip()
    if not url:
        return jsonify({"message": "No URL provided."}), 400

    try:
        response_message = str(out(url))  # Your existing URL processor
        return jsonify({"message": response_message})
    except Exception as e:
        return jsonify({"message": f"Error processing URL: {str(e)}"}), 500

@app.route('/process-question', methods=['POST'])
def process_question():
    data = request.get_json()
    question = data.get('question', '').strip()

    if not question:
        return jsonify({"message": "No question provided."}), 400

    try:
        # You can replace this with your own logic or model
        response_message = str(rag_qa(question))
        return jsonify({"message": response_message})
    except Exception as e:
        return jsonify({"message": f"Error processing question: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000)
