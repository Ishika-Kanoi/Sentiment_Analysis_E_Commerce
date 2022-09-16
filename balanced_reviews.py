# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 01:23:11 2022

@author: ishika
"""

import pandas as pd
#Data Preparation
df_reader = pd.read_json('Clothing_Shoes_and_Jewelry.json', chunksize=(1000000) , lines=True )

counter = 1
for chunk in df_reader:
    new_df =  pd.DataFrame(chunk[['overall','reviewText','summary']])
    #creating sample dataframes from chunk
    new_df1 = new_df[new_df['overall']== 1].sample(4000)
    new_df2 = new_df[new_df['overall']==2].sample(4000)
    new_df3 = new_df[new_df['overall']==4].sample(4000)
    new_df4 = new_df[new_df['overall']==5].sample(4000)
    new_df5 = new_df[new_df['overall']==3].sample(4000)
    #concatenating the Dataframes
    new_df6 = pd.concat([new_df1,new_df2,new_df3,new_df4,new_df5],axis=0,ignore_index=True)
    #saving into csv files
    new_df6.to_csv(str(counter)+'.csv', index = False)
    counter = counter+1
    
from glob import glob

filenames = glob('*.csv')
#concatenate the csv files
#emtylist dataframe
dflist = []
for file in filenames:
    dflist.append(pd.read_csv(file)) 
#dflist will have 33 dataframes
finaldf = pd.concat(dflist,axis = 0, ignore_index=True)
#changing created data object to csv
finaldf.to_csv("Balanced_reviews.csv", index = False)


