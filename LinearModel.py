import numpy as np
import pandas as pd
import statistics as st

class simpleLinearmodel():
    def __init__(self):
        self.w = np.random.randn(1)[0]
        self.b = np.random.randn(1)[0]
    def linear_regression(self,file):
        data = pd.read_csv(file)
        xmean = st.mean(data['YearsExperience'])
        ymean = st.mean(data['Salary'])
        xsum = pd.DataFrame.sum(data['YearsExperience'])
        ysum = pd.DataFrame.sum(data['Salary'])
        Sxx = pd.DataFrame.sum((data['YearsExperience'] - xmean)**2)
        Sxy = pd.DataFrame.sum((data['YearsExperience']- xmean)*(data['Salary']-ymean))
        print(Sxx)
        print(Sxy)
        return
    pass




