import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("student_dataset.csv")

# ✅ FIX: remove empty rows
data = data.dropna()

X = data[['hours','attendance','marks']]
y = data['result']

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully!")

