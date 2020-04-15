import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import json 

from filters import getFilter,search
from table import table
from charts import bigGraph,setBigGraphData,setSideChartsdata,sideCharts

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
                                html.Label('Model'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Model')      
                                        ],
                                        multi=True,
                                        id="model_search"
                                ),
                                ],
                className="inputs-container"),

                   html.Div(children=[       
                                html.Label('Mem'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Mem')      
                                        ],
                                        multi=True,
                                        id="mem_search"
                                ),
                                ],
                className="inputs-container"),


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

                html.Div(children=[       
                                html.Label('Dimms'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Dimms')      
                                        ],
                                        multi=True,
                                        id="dimms_search"
                                ),
                                ],
                className="inputs-container"),

                 html.Div(children=[       
                                html.Label('Threads'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Threads')      
                                        ],
                                        multi=True,
                                        id="threads_search"
                                ),
                                ],
                className="inputs-container"),

                 html.Div(children=[       
                                html.Label('Cores'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('Cores')      
                                        ],
                                        multi=True,
                                        id="cores_search"
                                ),
                                ],
                className="inputs-container"),

                 html.Div(children=[       
                                html.Label('TDP'),
                                 dcc.Dropdown(
                                        options=[
                                                {'label': v, 'value': v } for  v in getFilter('TDP')      
                                        ],
                                        multi=True,
                                        id="tdp_search"
                                ),
                                ],
                className="inputs-container"),
                
              ], className="input-group  d-flex justify-content-between mt-3 mb-2 "),
              ],id="header-content", className=" d-flex flex-column"),
              html.Button(children="Header", id="btn-show", className="btn btn-success")
        ],className='header d-flex flex-column  '),

#header end



#main start

        html.Div(children=[ 

        html.Div(children=[
                table()
         ], className="table-container"),

        html.Div(children=[  
                bigGraph(), 
                html.Div(children=[  
                        html.Div(children=[
                       
                        ],className="col-md-8"), 
                         html.Div(children=[
                        sideCharts('Vendor'),
                        sideCharts('Model'),
                        sideCharts('OS'),
                        sideCharts('Kernel'),
                        sideCharts('CPU'),
                        ],className="col-md-4 "), 
                 ], className="row pt-5" )
                         
        ], className="charts-container "),


          
        ], className="main")         
  
    
])



## update table data
@app.callback(
    [Output("table", "data")],
    [
     Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value')
    ]
)
def updateTable(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    

    return search(vendor=vendor_value, cpu=cpu_value, kernel=kernel_value, os=os_value, model=model_value, mem=mem_value, dimms=dimms_value, threads=threads_value, cores=cores_value,tdp=tdp_value).sort_values(by=['Score'],ascending=False).to_dict('records'),
#update table data end


#update big graph
@app.callback(
    Output("big-graph", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    Input("big-graph-y-param", 'value'),
    Input("big-graph-x-param", 'value')]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value,x_value, y_values):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=[x_value],ascending=False)

    return setBigGraphData(search_result, y_values, x_value)
#update big graph end

#update graph text output
@app.callback(
        Output('vendor_txt','children'),
        [Input('big-graph', 'hoverData')]
)
def display_hover_data(hoverData):
        if hoverData:
                vendor = hoverData['points'][0]['text']
                

                return vendor
@app.callback(
        Output('model_txt','children'),
        [Input('big-graph', 'hoverData')]
)
def display_hover_data(hoverData):
        if hoverData:
        
                model = hoverData['points'][0]['customdata']

                return model

#update side graph

@app.callback(
    Output("side-pie-graph-Vendor", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return setSideChartsdata(search_result,'Vendor')


@app.callback(
    Output("side-pie-graph-OS", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return setSideChartsdata(search_result,'OS')



@app.callback(
    Output("side-pie-graph-Model", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return setSideChartsdata(search_result,'Model')


@app.callback(
    Output("side-pie-graph-CPU", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return setSideChartsdata(search_result,'CPU')


@app.callback(
    Output("side-pie-graph-Kernel", "figure"),
    [Input("vendor_search", 'value'),
    Input("cpu_search", 'value'),
    Input("kernel_search", 'value'),
    Input("os_search", 'value'),
    Input("model_search", 'value'),
    Input("mem_search", 'value'),
    Input("dimms_search", 'value'),
    Input("threads_search", 'value'),
    Input("cores_search", 'value'),
    Input("tdp_search", 'value'),
    ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return setSideChartsdata(search_result,'Kernel')

#show and hide header 

@app.callback(Output('header-content', 'className'), [Input('btn-show', 'n_clicks')])
def on_click(data):

        if  data == None or data % 2 == 0  :
                return "hide"
        else :
                return "visible"


     

if __name__ == '__main__':
    app.run_server(debug=True)