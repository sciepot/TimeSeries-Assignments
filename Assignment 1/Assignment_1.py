import numpy as np  #for numeric computations like log, exp, sqrt
import pandas as pd #for reading & storing data, pre=processing
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt #for visualization
import statsmodels.api as sm
from scipy import stats

data = pd.read_csv('DATA.csv', index_col='DATE')
data.index = pd.to_datetime(data.index)
print(data.index)
data.plot()
