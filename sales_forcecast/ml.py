import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

import sys
df=pd.read_csv("sales.csv",index_col=['date'],parse_dates=['date'])
p=sys.argv[1][0]
c=sys.argv[2]
df=df.dropna()
ts=df['Global_Sales'].resample(p).sum()
import warnings
warnings.filterwarnings('ignore')
model1=ARIMA(ts, order=(5,0,4)).fit()
prediction=model1.predict(len(ts),len(ts)+int(c))
ts.plot(legend=True, label='Train',figsize=(10,6))
prediction.plot(legend=True, label='prediction')
plt.savefig('project/src/assets/temp.png')
ts.to_csv("cleaned_data.csv")
