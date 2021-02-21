from LinearModel import simpleLinearmodel
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

newModel = simpleLinearmodel()
a, b = newModel.linear_regression('Salary_Data.csv')
data = pd.read_csv('Salary_Data.csv')
x = np.linspace(0, 15, 100)
y = (a*x) + b 
plt.scatter(data['YearsExperience'],data['Salary'])
plt.plot(x,y, 'r')
plt.show()