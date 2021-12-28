def predict():
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    import numpy as np
    import requests
    import json

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    url = 'http://localhost:8080/predict'
    headers = {
        'Content-type': "application/json"
    }

    data = json.dumps(X_test.tolist())
    response = requests.post(url, headers=headers, data=data)
    predictions = np.array(json.loads(response.text))
    print(f'Predictions: {predictions}')
    print(f'Accuracy Score: {accuracy_score(predictions, y_test)}')

if __name__ == '__main__':
    predict()