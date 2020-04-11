import pandas as pd
import numpy as np
all_data = pd.read_csv('data/SpeCopyspec.csv')
def getFilter(index):
   
    return   all_data[index].unique()
