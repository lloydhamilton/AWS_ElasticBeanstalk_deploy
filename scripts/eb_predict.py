def eb_predict():
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    import numpy as np
    import requests
    import json

    # Load data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into test and training set
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Define url and headers
    url = 'http://flask-api-dev.eu-west-2.elasticbeanstalk.com/predict'
    headers = {
        'Content-type': "application/json"
    }

    # Package data as JSON to pass in POST HTTP request.
    data = json.dumps(X_test.tolist())
    response = requests.post(url, headers=headers, data=data)

    # Parse response as JSON and return predictions
    predictions = np.array(json.loads(response.text))
    print(f'Predictions: {predictions}')
    print(f'Accuracy Score: {accuracy_score(predictions, y_test)}')

if __name__ == '__main__':
    eb_predict()