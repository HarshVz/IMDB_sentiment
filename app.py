from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the comment from the request
    data = request.json
    comment = data.get('comment', '')

    # Make a prediction
    prediction = model.predict([comment])

    return jsonify({'comment': comment, 'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
