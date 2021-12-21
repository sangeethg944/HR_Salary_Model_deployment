#imported necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("salarydata.csv")
df = df[['age', 'hours-per-week', 'workclass', 'education', 'marital-status', 'occupation',
       'relationship', 'race', 'sex', 'native-country','salary']]
df.drop(df[df['workclass'] == '?'].index, inplace = True)
df.drop(df[df['occupation'] == '?'].index, inplace = True)
df.drop(df[df['native-country'] == '?'].index, inplace = True)
target_salary = df.pop('salary')

label = {}
for c in df.iloc[:,2:].columns:
   df[c], label[c] = pd.factorize(df[c])


#Random Forest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

x_train, x_test, y_train, y_test = train_test_split(df, target_salary)


model = RandomForestClassifier(n_estimators=20)
model.fit(x_train, y_train)


def classify(a,b,c,d,e,f,g,h,i,j):
    arr = np.array([a,b,c,d,e,f,g,h,i,j])
    input_ = arr.reshape(1, -1)
    prediction = model.predict(input_)
    return prediction[0]

