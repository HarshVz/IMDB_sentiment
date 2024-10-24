import json
import pickle
from flask import Flask, request
from flask_cors import CORS  # Import CORS

# Load the model
with open('./sentiment_model.pkl', 'rb') as f:  # Adjust the path if necessary
    model = pickle.load(f)

app = Flask(__name__)

# Initialize CORS
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    comment = data.get('comment', '')

    if not comment:
        return json.dumps({'error': 'No comment provided.'}), 400

    prediction = model.predict([comment])
    return json.dumps({'comment': comment, 'prediction': prediction[0]})

# Vercel serverless function handler
def handler(req, res):
    return app(req, res)

if __name__ == '__main__':
    app.run(debug=True)  # Optional for local testing
