# this file contain codes about the charts
import dash
import dash_core_components as dcc
import dash_html_components as html
from filters import getNumericCol
import pandas as pd
def bigGraph():
    graph = html.Div(
            
            children=[
                        html.Div(children=[

                            html.Div(children=[
                                html.Label("Vendor : "),
                                html.Div( id="vendor_txt"),
                                html.Label("Model : ", className="pt-3"),
                                html.Div( id="model_txt"),
                                                              
                            ], className="big-graph-output-container"),

                            html.Div(children=[
                                
                                    html.Div(children=[
                                        html.Label('Y parameters'), 
                                        dcc.Checklist(
                                        options=[
                                            {'label': v, 'value': v} for v in getNumericCol()
                                        
                                        ],
                                        value=['Cores', 'Threads', 'Cores.1'],
                                        id="big-graph-x-param",
                                        labelStyle={'display': 'flex'}
                                    )
                            ], className="form-check"),

                            html.Div(children=[
                                html.Label('X parameters'), 
                                    dcc.RadioItems(
                                        options=[
                                            {'label': v, 'value': v} for v in getNumericCol()
                                        
                                        ],
                                        value='Score',
                                        id="big-graph-y-param",
                                        labelStyle={'display': 'flex'}
                                    ) 
                            ], className="form-check")
                            

                            ], className="big-grah-param" ),
                        ],className="big-grah-param-container"),
                        

                        
                        dcc.Graph(
                            id='big-graph',
                         
                        
                        )  
            ], className="big-graph-container d-flex flex-row"
    )
    return  graph

def setBigGraphData(data, yaxis, x):
    
    return {  'data': [{
                        'x': [d for d in data[x]], 
                        'y': [d for d in data[y]], 
                        'customdata': [d for d in data['Model']],
                        'type': 'line', 'name': str(y),
                        'text' : [d for d in data['Vendor']]
                        
                    } for y in list(yaxis)],
            'layout':
            {
                'title': 'Find relations between numeric parameters',
                "height":"30rem",
                "width":  850,
                'clickmode': 'event+select',
               
                
            }
    }