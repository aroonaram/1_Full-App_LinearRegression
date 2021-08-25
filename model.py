# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sb
from sklearn.preprocessing import MinMaxScaler

df =  pd.read_csv(
    'ElectricBill.csv', sep=",",header=0, index_col=None, usecols=None, parse_dates=['Date'])

x1= df['Average kWh']
x2 = df['Fuel Charge (Cents/kWh)']
y = df['Average Bill']
x1= x1.values.reshape(-1,1)
x2= x2.values.reshape(-1,1)
y= y.values.reshape(-1,1)



scaler = MinMaxScaler()

# Normalization
scaler = MinMaxScaler()
x1 = scaler.fit_transform(x1)
x2 = scaler.fit_transform(x2)

y = scaler.fit_transform(y)

df['Average kWh'] = x1
df['Fuel Charge (Cents/kWh)'] = x2
X = df.iloc[:, 1:3]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

pred_val = model.predict([[.829,0.1]])

print((pred_val[0])*100)

