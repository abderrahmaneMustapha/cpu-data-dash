import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

from filters import getFilter
all_data = pd.read_csv('data/SpeCopyspec.csv')


app = dash.Dash()

app.layout = html.Div(children=[
      
        html.Div(children=[ 

            html.Div(children=[ html.H1(children='CPU Data Dashboard')]),

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
                
                html.Div(children=[       
                                html.Label('CPU'),
                                dcc.Input(id='cpu_input', value='Enter a cpu name here here!', type='text'),],
                className="inputs-container")
            ])

        ], className='header'),
              
                  
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
    )]),
    
])



if __name__ == '__main__':
    app.run_server(debug=True)