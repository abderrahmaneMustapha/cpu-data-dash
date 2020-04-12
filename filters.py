import pandas as pd
import numpy as np
all_data = pd.read_csv('data/SpeCopyspec.csv').dropna(axis=1, how='any', thresh=None, subset=None, inplace=False).drop(columns='URL')
def getFilter(index):
   
    return   all_data[index].unique()


def search(vendor=None,kernel=None,os=None,cpu=None):
    result = all_data.copy()
    result.set_index(['Vendor', 'Kernel', 'OS', 'CPU'], inplace=True)
    
    
    return result.loc[(('Tyrone'),('4.12.14-25.13-default', '3.10.0-1062.el7.x86_64'), ('CentOS Linux 7 (Core)')), :].reset_index()


print(search())