from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import joblib
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

def display_scores(scores):
    print("Scores:", scores)
    print("Means:", scores.mean())
    print("Standard Deviation:", scores.std())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_clf = RandomForestClassifier()
rf_clf.fit(X_train, y_train)
rf_scores = cross_val_score(rf_clf, X_train, y_train, scoring = 'accuracy', cv = 3)
display_scores(rf_scores)
joblib.dump(rf_clf, 'models/rf_clf.joblib')
