# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Import my fiancial data class
from IntrinioAPIGetStockPriceData import StockData



## Dash Application ##
# Dash framwork
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = [
html.Div(children="Input Ticker: "),
        dcc.Input(id='ticker', value='', type='text'),
        html.Div(id='price_graph'),
])

@app.callback(
    Output(component_id='price_graph', component_property='children'),
    [Input(component_id='ticker', component_property='value')]
)
def update_priceGraph(input_ticker):
    ## Call fiancial Data ##
    TickerStockData = StockData(input_ticker, 300) # Ticker and number of trading days to query for
    TickerStockData.getStockData() # populate with data from ticker
    return dcc.Graph(id = TickerStockData.identifier + ' Price Data',
              figure = {
                      'data': [
                              {'x' : TickerStockData.correspondingDates[0:len(TickerStockData.correspondingDates) -1], 'y' : TickerStockData.priceData[0:len(TickerStockData.priceData)-1], 'type':'line', 'name':TickerStockData.identifier},
                              ],
                      'layout': {
                              'title': TickerStockData.identifier + ' Price Data Over the Past ' + str(TickerStockData.dayCount) + ' Trading Days'
                              }
                      })


if __name__ == '__main__':
    app.run_server(debug = True)
