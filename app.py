import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import pandas as pd

from filters import getFilter,search
from table import table
from charts import bigGraph,setBigGraphData

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(children=[
      
        html.Div(children=[ 
           
            html.Div(children=[ html.H1(children='CPU Data Dashboard')], className="brand text-center mb-5"),
            html.Label('CPU Search'), 
            html.Div(children=[      
                           
                             dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('CPU')      
                                        ],
                                        multi=True,
                                        id="cpu_search"
                            ),
                            ],
            className="search-container"),
    

            html.Div(children= [
                html.Div(children=[
                                html.Label('Vendors'),
                                dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Vendor')      
                                        ],
                                        multi=True,
                                        id="vendor_search"
                                ),
                ], className="inputs-container"),
                
                html.Div(children=[
                                html.Label('Kernel'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Kernel')      
                                        ],
                                        multi=True,
                                        id="kernel_search"
                                ),
                ],className="inputs-container"),
                
                html.Div(children=[       
                                html.Label('OS'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('OS')      
                                        ],
                                        multi=True,
                                        id="os_search"
                                ),
                                ],
                className="inputs-container"),
                
              ], className="input-group  d-flex justify-content-between mt-3 mb-2 ")

        ], className='header d-flex  flex-column'),


        html.Div(children=[ 

            html.Div(children=[
               table()

            ], className="table-container"),
            html.Div(children=[  

              bigGraph()
               
            ], className="charts-container")
    ], className="main")         
  
    
])



## update table data
@app.callback(
    [Output("table", "data")],
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value')]
)
def updateTable(vendor_value, cpu_value, kernel_value, os_value):
    

    return search(vendor_value,kernel_value,os_value,cpu_value).sort_values(by=['Score'],ascending=False).head(n=20).to_dict('records'),
#update table data end

@app.callback(
    Output("big-graph", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("big-graph-y-param", 'value'),
    Input("big-graph-x-param", 'value')]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value,x_value, y_values):
    search_result = search(vendor_value,kernel_value,os_value,cpu_value).sort_values(by=[x_value],ascending=False)

    return setBigGraphData(search_result, y_values, x_value)

if __name__ == '__main__':
    app.run_server(debug=True)