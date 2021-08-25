import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict():
    title = 'Here is the prediction'
    int_features = [float(x) for x in request.form.values()]
    final_features = [no.array(int_features)]
    Prediction = model.predict(final_features)
    output = rount(prediction[0],2)
    return render_template('result.html' , prediction_text = 'Bill should be {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

