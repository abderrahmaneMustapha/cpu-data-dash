#this file contain codes about filters and search

#import
import pandas as pd
import numpy as np
#end import 


#open the csv file and drop null values  drop URL column too
all_data = pd.read_csv('data/SpeCopyspec.csv').dropna(axis=1, how='any', thresh=None, subset=None, inplace=False).drop(columns='URL')


#get row values by column  we will use the values to autocomplete the search 

def getFilter(index):   
    return   all_data[index].unique()

# get the filters that we are going to use in the big graph (only numeric columns)
def getNumericCol():
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return all_data.select_dtypes(include=numerics)



# searching 
def search(vendor=None,cpu=None,kernel=None,os=None,model=None,mem=None,dimms=None,threads=None,cores=None,tdp=None):
    
    
    result = all_data.copy()

    # check if one of the lists kernel, vendor, os , cpu
    if vendor or kernel or os  or cpu or model or mem or dimms or threads or cores or tdp:
        
        #put each data list and its column in this list
        values = [
                {'data' : vendor, 'key' : "Vendor"}, 
                {'data' : kernel, 'key': 'Kernel'}, 
                {'data': os, 'key':'OS'},
                {'data':cpu, 'key' : 'CPU'},
                {'data':model, 'key':'Model'},
                {'data':mem, 'key':'Mem'},
                {'data':dimms, 'key':'Dimms'},
                {'data':threads, 'key':'Threads'},
                {'data':cores, 'key':'Cores'},
                {'data':tdp, 'key':'TDP'},
                ]
        
        #list of the indexes
        indxes = []

        #list of data
        locations = []
        
        #loop through the values list  and check if the list is not empty
        for v in values:
            if v['data'] :
                #if the data list is not empty

                #add the column name to the indexes list
                indxes.append(v['key'])

                #and the data to the data list
                locations.append( tuple((i) for i in v['data']))
        
        
        #set the indexes
        result.set_index(indxes, inplace=True)
       
        #we have only a one index 
        if len(indxes) > 1:
            return result.loc[tuple(locations), :].reset_index()
        
        #here we have multi indexes
        else : 
            return result.loc[tuple(locations)].reset_index()
    #if all the lists is null 
    return result

def findMaxByGroup(params, by="best"):
    if by == "best":
        data_temp =all_data.sort_values(['Score'],ascending=False).groupby(params).head().head(20)
    else:
        data_temp =all_data.sort_values(['Score'],ascending=False).groupby(params).tail().tail(20)
    return  data_temp