
import joblib
import numpy as np
from flask import Flask, request
from flask import Response
import json

# model = None
app = Flask(__name__)

@app.route('/predict')
def predict_endpoint():
    test_data = request.get_json()
    test_data = np.array(test_data)
    predictions = model.predict(test_data)
    response = json.dumps(predictions.tolist())
    return Response(response, status=200, mimetype="application/json")

if __name__ == '__main__':
    model = joblib.load('rf_clf.joblib')
    app.run(host='0.0.0.0', port=80)
