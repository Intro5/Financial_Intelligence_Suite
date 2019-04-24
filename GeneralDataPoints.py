import pandas as pd
import numpy
from scipy.stats import linregress
import plotly as plt

aaplCoreData = pd.read_csv("/Users/torinbakos/Documents/ComputerScienceCapstone/csvFiles/EOD-AAPL.csv")
msftCoreData = pd.read_csv("/Users/torinbakos/Documents/ComputerScienceCapstone/csvFiles/EOD-MSFT.csv")

# linregress(aaplCoreData, msftCoreData)

# bring adjusted close values into list
aaplData = aaplCoreData['Adj_Close'].values.tolist()
msftData = msftCoreData['Adj_Close'].values.tolist()

#bring date values into list
aaplDates = aaplCoreData['Date'].values.tolist()
msftDates = msftCoreData['Date'].values.tolist()

# calculate percent change
aaplPercentChange = aaplCoreData['Adj_Close'].pct_change()
print(aaplPercentChange)
#print(aaplData[0:50])
#print(msftData)
#print(outputData)
#plt.plot(aaplData[0:50])
#plt.plot(aaplData[0:50])
#plt.show()
