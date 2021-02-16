import numpy as np
import pandas as pd
import statistics as st
import math

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
        a = Sxy/Sxx
        b = ymean - (xmean*a)
        Syy = pd.DataFrame.sum((data['Salary'] - ymean)**2)
        data['Yhat'] = (data['YearsExperience']*a)+b
        print(data)
        return a,b
    def find_r(self,a,b,file):
        data = pd.read_csv(file)
        ymean = st.mean(data['Salary'])
        ysum = pd.DataFrame.sum(data['Salary'])
        Syy = pd.DataFrame.sum((data['Salary'] - ymean)**2)
        data['Yhat'] = (data['YearsExperience']*a)+b
        yhatmean = st.mean(data['Yhat'])
        print(data)
        Syyhat = pd.DataFrame.sum((data['Salary'] - ymean)*(data['Yhat']-yhatmean))
        Syhatyhat =   pd.DataFrame.sum((data['Yhat'] - yhatmean)**2)
        R = Syyhat/ math.sqrt(Syy*Syhatyhat)
        return R
    pass




