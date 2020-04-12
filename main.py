import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import pandas as pd

from filters import getFilter
from table import table
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        'crossorigin': 'anonymous'
    }
]
app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
      
        html.Div(children=[ 
           
            html.Div(children=[ html.H1(children='CPU Data Dashboard')], className="brand text-center mb-5"),
            html.Label('CPU Search'), 
            html.Div(children=[      
                           
                            dcc.Input(id='cpu_input', placeholder='Enter a cpu name here here!', type='text', className="form-control"),
                            html.Button(id='search_btn', n_clicks=0, children='Submit', className="btn btn-light"),
                            ],
            className="search-container"),
            html.Div(id='output-state'),

            html.Div(children= [
                html.Div(children=[
                                html.Label('Vendors'),
                                dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Vendor')      
                                        ],
                                        multi=True,
                                ),
                ], className="inputs-container"),
                
                html.Div(children=[
                                html.Label('Kernel'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Kernel')      
                                        ],
                                        multi=True,
                                ),
                ],className="inputs-container"),
                
                html.Div(children=[       
                                html.Label('OS'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('OS')      
                                        ],
                                        multi=True,
                                ),
                                ],
                className="inputs-container"),
                
              ], className="input-group  d-flex justify-content-between mt-3 mb-2 ")

        ], className='header d-flex  flex-column'),


        html.Div(children=[ 

            html.Div(children=[
               table()

            ], className="table-container"),
            html.Div(children=[  dcc.Graph(
                id='example',
                    figure={
                        'data': [
                            {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'bar', 'name': 'Something'},
                        
                        ],
                        'layout': {
                            'title': 'Test'
                        }
                    }
            )])
    ], className="main")         
  
    
])


@app.callback(Output('output-state', 'children'),
              [Input('search_btn', 'n_clicks')],
              [State('cpu_input', 'value')])
def update_output(n_clicks, input1):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
    '''.format(n_clicks, input1)



if __name__ == '__main__':
    app.run_server(debug=True)