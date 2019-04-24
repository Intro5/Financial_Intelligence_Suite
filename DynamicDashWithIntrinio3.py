# Dash imports
import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
from dash.dependencies import Input, Output


# Import pandas and numpy
import pandas as pd
import numpy as np

# Import my fiancial data class
from IntrinioAPIStandardizedFinancials import FundamentalData

## Get Fundamental Data and place into dataframe
Stock_FinancialData = FundamentalData('AAPL', 2018)
Stock_FinancialData.getFinancialData()
balance_sheet_statement_DF = pd.DataFrame(list(Stock_FinancialData.balance_sheet_statement.items()), columns=['Line Item', 'Value in USD'])
income_statement_DF = pd.DataFrame(list(Stock_FinancialData.income_statement.items()), columns=['Line Item', 'Value in USD'])
cash_flow_statement_DF = pd.DataFrame(list(Stock_FinancialData.cash_flow_statement.items()), columns=['Line Item', 'Value in USD'])




## Dash Application ##
# Dash framwork
def generate_table(dataframe, max_rows=30):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H4(children='Balance Sheet Statement'),
    generate_table(balance_sheet_statement_DF),
    html.H4(children='Income Statement'),
    generate_table(income_statement_DF),
    html.H4(children='Cash Flow Statement'),
    generate_table(cash_flow_statement_DF),
])

if __name__ == '__main__':
    app.run_server(debug = True)
