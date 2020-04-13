import pandas as pd
import numpy as np
all_data = pd.read_csv('data/SpeCopyspec.csv').dropna(axis=1, how='any', thresh=None, subset=None, inplace=False).drop(columns='URL')
def getFilter(index):
   
    return   all_data[index].unique()


def search(vendor=['ASUS'],kernel=None,os=None,cpu=None):
    result = all_data.copy()
    if vendor is None and kernel is None and os is None and cpu is None:
        return result
    values = [
            {'data' : vendor, 'key' : "Vendor"}, 
            {'data' : kernel, 'key': 'Kernel'}, 
            {'data': os, 'key':'OS'},
            {'data':cpu, 'key' : 'CPU'}
            ]
    indxes = []
    locations = []

    for v in values:
        if v['data'] :
            indxes.append(v['key'])
            locations.append( tuple((i) for i in v['data']))

    result.set_index(indxes, inplace=True)
    
    if len(indxes) > 1:
        return result.loc[tuple(locations), :].reset_index()
    else : 
        return result.loc[tuple(locations)].reset_index()


print(search())