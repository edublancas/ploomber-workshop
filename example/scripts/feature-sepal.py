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

# Generates sepal features.

import pandas as pd

# + tags=["parameters"]
upstream = ['get']
product = None
# -


df = pd.read_csv(upstream['get']['data'])

df.head()

df['sepal-area'] = df['sepal length (cm)'] * df['sepal width (cm)']

df[['sepal-area']].to_csv(product['data'], index=False)


