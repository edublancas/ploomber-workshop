# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Train a model.

from pathlib import Path
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn_evaluation import plot

# + tags=["parameters"]
upstream = ['get', 'feature-sepal', 'feature-petal']
product = None
# -


get = pd.read_csv(upstream['get']['data'])

petal = pd.read_csv(upstream['feature-sepal']['data'])

sepal = pd.read_csv(upstream['feature-petal']['data'])

df = get.join(petal).join(sepal)

X = df.drop('target', axis='columns')
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plot.confusion_matrix(y_test, y_pred)

Path(product['model']).write_bytes(pickle.dumps(model))