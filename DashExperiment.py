#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:37:36 2019

@author: torinbakos
"""
# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html

# Conda imports
import pandas as pd
import numpy
from scipy.stats import linregress



# read csv
aaplCoreData = pd.read_csv("/Users/torinbakos/Documents/ComputerScienceCapstone/csvFiles/EOD-AAPL.csv")
msftCoreData = pd.read_csv("/Users/torinbakos/Documents/ComputerScienceCapstone/csvFiles/EOD-MSFT.csv")

# linregress(aaplCoreData, msftCoreData)

# bring adjusted close values into list
aaplData = aaplCoreData['Adj_Close'].values.tolist()
msftData = msftCoreData['Adj_Close'].values.tolist()

#bring date values into list
aaplDates = aaplCoreData['Date'].values.tolist()
msftDates = msftCoreData['Date'].values.tolist()


# Dash framwork
app = dash.Dash()

app.layout = html.Div(children = [
        html.H1('Microsoft and Apple'),
        dcc.Graph(id = 'AAPL Price Data',
                  figure = {
                          'data': [
                                  {'x' : aaplDates[0:365], 'y' : aaplData[0:365], 'type':'line', 'name':'AAPL'},
                                  ],
                          'layout': {
                                  'title':'AAPL Price Data Over the Past 365 Business Days'
                                  }
                          }),

     dcc.Graph(id = 'MSFT Price Data',
                  figure = {
                          'data': [
                                  {'x' : msftDates[0:365], 'y' : msftData[0:365], 'type':'line', 'name':'AAPL'},
                                  ],
                          'layout': {
                                  'title':'MSFT Price Data Over the Past 365 Business Days'
                                  }
                          })

])

if __name__ == '__main__':
    app.run_server(debug = True)
