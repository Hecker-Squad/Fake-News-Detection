from flask import Flask, request, jsonify
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['input_data']
    vectorized_input_data = tfidf_vectorizer.transform(input_data)
    prediction = model.predict(vectorized_input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
