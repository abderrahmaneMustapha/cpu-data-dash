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



# searching 
def search(vendor=None,kernel=None,os=None,cpu=None):
    
    
    result = all_data.copy()

    # check if one of the lists kernel, vendor, os , cpu
    if vendor or kernel or os  or cpu :
        
        #put each data list and its column in this list
        values = [
                {'data' : vendor, 'key' : "Vendor"}, 
                {'data' : kernel, 'key': 'Kernel'}, 
                {'data': os, 'key':'OS'},
                {'data':cpu, 'key' : 'CPU'}
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


print(search())