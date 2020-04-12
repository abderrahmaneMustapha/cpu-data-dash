import dash_table
import pandas as pd
all_data = pd.read_csv('data/SpeCopyspec.csv').dropna(axis=1, how='any', thresh=None, subset=None, inplace=False).drop(columns='URL')
 
def table():
    
    
    
    
    table = dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i,'deletable': True} for i in all_data],
                data=all_data.sort_values(by=['Score'],ascending=False).head(n=10).to_dict('records'),
                style_table={
                    'overflowX': 'scroll',
                    'width': '100%'
                },
                filter_action="native",
                sort_action="native",
                style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'minWidth': '5rem',
                },
    )


    return table