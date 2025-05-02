from random import seed
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier


# Read original dataset
iris_df = pd.read_csv("data/iris.csv")
iris_df.sample(frac=1, random_state=42)
# selecting features and target data
X = iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris_df[['Class Label']]
# split data into train and test sets
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=42, stratify=y)
# create an instance of the random forest classifier
clf = RandomForestClassifier(n_estimators = 100)
# traing the classifier on the traning data
clf.fit(X_train, y_train)
# predict on the test set
y_pred = clf.predict(X_test)
# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}") # Accuracy: 0.91

# save the model to disk
import joblib

joblib.dump(clf, "rf_model.sav")
