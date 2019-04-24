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
from dash.dependencies import Input, Output

# Intrinio and related imports
import time
from datetime import datetime, date, timedelta
import intrinio_sdk
from intrinio_sdk.rest import ApiException



# StockData imports
import time
from datetime import datetime, date, timedelta
import intrinio_sdk
from intrinio_sdk.rest import ApiException

# set up intrinio accsess
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjlmODA4ZTJjZTQ0ZTIxNTUyYmZjNDY5NTc2MWNmY2Q0'

security_api = intrinio_sdk.SecurityApi()

# Get Data from intrinio
dayCount = 730
identifier = 'AAPL' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
start_date = str(date.today() - timedelta(days = dayCount)) # date | Get historical data on or after this date (optional)
end_date = str(date.today()) # date | Get historical date on or before this date (optional)
frequency = 'daily' # str | Sort by date `asc` or `desc` (optional)
next_page = '' # str | Gets the next page of data from a previous API call (optional)
page_size = dayCount
priceData = []
correspondingDates = []

try:
    api_StockPriceResponse = security_api.get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, page_size=page_size).__dict__
    list_of_StockPriceDicts = api_StockPriceResponse['_stock_prices']
    i = 0
    while i < len(list_of_StockPriceDicts):
        priceData.append(list_of_StockPriceDicts[i].__dict__['_adj_close'])
        correspondingDates.append(list_of_StockPriceDicts[i].__dict__['_date'])
        i += 1
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_historical_data: %s\n" % e)


# Dash framwork
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = [
        html.H1(identifier),
        dcc.Graph(id = identifier + ' Price Data',
                  figure = {
                          'data': [
                                  {'x' : correspondingDates[0:len(correspondingDates) -1], 'y' : priceData[0:len(priceData)-1], 'type':'line', 'name':'AAPL'},
                                  ],
                          'layout': {
                                  'title': identifier + ' Price Data Over the Past 365 Business Days'
                                  }
                          }),

])


if __name__ == '__main__':
    app.run_server(debug = True)
