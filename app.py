from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model/clv_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        aov = float(request.form['aov'])
        frequency = float(request.form['frequency'])
        lifespan = float(request.form['lifespan'])

        features = np.array([[aov, frequency, lifespan]])
        prediction = model.predict(features)[0]

        return render_template('index.html',
                               prediction_text=f"Estimated CLV: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)


