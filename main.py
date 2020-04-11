import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='CPU Data'),
    dcc.Graph(
        id='example',
            figure={
                'data': [
                    {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'bar', 'name': 'Something'},
                
                ],
                'layout': {
                    'title': 'Test'
                }
            }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)