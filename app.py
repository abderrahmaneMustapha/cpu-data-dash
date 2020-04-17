import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import json 

from filters import getFilter,search,getNumericCol
from table import table
from charts import bigGraph,setBigGraphData,setSideChartsdata,sideCharts,barChartsData,barCharts,scatterChart,scatterChartsData

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
                html.H3(children="Correlation between parameters", className="text-center col-md-12 mt-5 "),
                html.Div(children=[
                                        html.Label('Group By', className="text-center ml-5 mr-5"), 
                                       dcc.Dropdown(
                                        options=[
                                            {'label': 'Vendor', 'value': 'Vendor'},
                                            {'label': 'Model', 'value': 'Model'},
                                            {'label': 'Kernel', 'value': 'Kernel'},
                                            {'label': 'OS', 'value': 'OS'},
                                            {'label': 'CPU', 'value': 'CPU'},
                                        
                                        ],
                                        value='Vendor',
                                        id="scatter-graph-group-param",
                                        multi=False,
                                        className="mb-3 ml-5 mr-5"
                                    )
                ],),
                 scatterChart(),
                html.Div(children=[  
                         html.H3(children='Best and worst Vendors, Kernel, OS , Model,CPU',className="text-center"),
                        html.Div(children=[
                          
                           #param container
                           html.Div(children=[
                                html.Div(children=[
                                        html.Label('Group By', className="ml-5 mr-5"), 
                                       dcc.Dropdown(
                                        options=[
                                            {'label': 'Vendor', 'value': 'Vendor'},
                                            {'label': 'Model', 'value': 'Model'},
                                            {'label': 'Kernel', 'value': 'Kernel'},
                                            {'label': 'OS', 'value': 'OS'},
                                            {'label': 'CPU', 'value': 'CPU'},
                                        
                                        ],
                                        value=['Vendor'],
                                        id="bar-graph-group-param",
                                        multi=True,
                                        className="ml-5 mr-5"
                                    )
                                ],),
                                html.Div(children=[
                                        html.Label('Y parameters', className="ml-5 mr-5"), 
                                        dcc.Dropdown(
                                                options=[
                                                {'label': v, 'value': v} for v in getNumericCol()
                                                
                                                ],
                                                value='Score',
                                                id="bar-graph-x-param",
                                                multi=False,
                                                className="ml-5 mr-5"
                                        ) 
                                ], )
                           ], className="col-md-12"),
                            #param container end
                             #bar graphs container
                           html.Div(children=[
                                   barCharts(id="best-vendors-bar"),
                                   barCharts(id="worst-vendors-bar")
                           ], className="row col-md-9"),
                           #bar graphs container end


                        ],className="col-md-12"), 
                        html.Div(children=[
                        html.H3(children='Number of  Vendors, Kernel, Model, CPU ... in the dataset ',className="text-center  w-100 col-md-12"),
                        html.P(children='you can filter this data using the parameters in the header',className="text-center  w-100 col-md-12"),
                        sideCharts('Vendor'),
                        sideCharts('Model'),
                        sideCharts('OS'),
                        sideCharts('Kernel'),
                        sideCharts('CPU'),
                        sideCharts('Ver'),
                        sideCharts('Dimms'),
                        sideCharts('Cores'),
                        ],className="col-md-12 row "), 
                 ], className="row pt-5 d-flex justify-content-center flex-row" ),

                
                       
              
                         
        ], className="charts-container"),


          
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


@app.callback(
    Output("side-pie-graph-Ver", "figure"),
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

    return setSideChartsdata(search_result,'Ver')

@app.callback(
    Output("side-pie-graph-Dimms", "figure"),
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

    return setSideChartsdata(search_result,'Dimms')

@app.callback(
    Output("side-pie-graph-Cores", "figure"),
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

    return setSideChartsdata(search_result,'Cores')

#show and hide header 

@app.callback(Output('header-content', 'className'), [Input('btn-show', 'n_clicks')])
def on_click(data):

        if  data == None or data % 2 == 0  :
                return "hide"
        else :
                return "visible"

@app.callback(
    Output("best-vendors-bar", "figure"),
    [Input("bar-graph-group-param", 'value'),
    Input("bar-graph-x-param", 'value')]
)
def updateBestTable(param,y_value):
        return barChartsData(param,y_value,"best")

@app.callback(
    Output("worst-vendors-bar", "figure"),
    [Input("bar-graph-group-param", 'value'),
    Input("bar-graph-x-param", 'value')]
)
def updateBestTable(param,y_value):
        return barChartsData(param,y_value,"worst")

#update scatter plot graph

@app.callback(
    Output("scatter-graph", "figure"),
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
    Input("scatter-graph-x-param", 'value'),
    Input("scatter-graph-y-param", 'value'),
    Input("scatter-graph-group-param", 'value'),
   ]
)
def updateGraph(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value,x_value, y_values, param):
    search_result = search(vendor_value, cpu_value, kernel_value, os_value, model_value, mem_value, dimms_value, threads_value, cores_value,tdp_value).sort_values(by=['Score'],ascending=False)

    return scatterChartsData(search_result, y_values, x_value, param)

if __name__ == '__main__':
    app.run_server(debug=True)