from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    comment = data.get('comment', '')

    if not comment:
        return json.dumps({'error': 'No comment provided.'}), 400

    prediction = model.predict([comment])

    # Convert the prediction to a standard Python integer if it's an int64
    prediction_value = int(prediction[0])  # Ensure it's a standard int

    return json.dumps({'comment': comment, 'prediction': prediction_value})

if __name__ == '__main__':
    app.run(debug=True)
