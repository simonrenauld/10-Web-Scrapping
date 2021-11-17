# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:32:45 2021

Sources: 
https://www.back4app.com/database/back4app/occupations-and-job-titles   
    

@author: renau
"""


#Libraries
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import matplotlib.pyplot as plt
from tabulate import tabulate
import re 
import numpy as np
##################################
# GET JOBS Linkedin 

dftitle = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\webscrapping\linkedin\outputs\Results\outputsallVietnamtest.csv', encoding="utf8")
dfdescription = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\webscrapping\linkedin\outputs\Results\outputsalldescriptionsVietnam.csv',encoding='utf-8-sig')

print(dftitle.info())
print(dfdescription.info())


DFMerge = dftitle.merge(dfdescription, left_on='Link', right_on='Link', how='inner')
print(DFMerge.info())
print(DFMerge.head())

#---------------- to delete
DFMerge.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\webscrapping\linkedin\outputs\Analysis\test.csv',encoding='utf-8-sig')    

##################################
# GET JOBS Title Database and Categories 

JOB = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\job.csv', encoding="utf8")
SOCBroadGroup = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\SOCBroadGroup.csv',encoding='utf-8-sig')
SOCDetailedGroup = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\SOCDetailedGroup.csv',encoding='utf-8-sig')
SOCMajorGroup = pd.read_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\SOCMajorGroup.csv',encoding='utf-8-sig')


SOCJobMerge = JOB.merge(SOCDetailedGroup, left_on='SOCDetailedGroup', right_on='SOCDetailedGroup', how='inner')
SOCJobMerge = SOCJobMerge.merge(SOCBroadGroup, left_on='broadGroup', right_on='broadGroup', how='inner')
SOCJobMerge['title'] = SOCJobMerge['title'].str.lower()

#---------------- to delete
SOCJobMerge.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\SOCJobMerge.csv',encoding='utf-8-sig')   


##################################
# Fuzzy Matching SCRAPPING Vs JobsDatabase

print(tabulate(DFMerge.head(2), headers='keys', tablefmt='psql'))
print(tabulate(SOCJobMerge.head(2), headers='keys', tablefmt='psql'))


compare = pd.MultiIndex.from_product([DFMerge['Title'],
                                      SOCJobMerge['title']]).to_series()

def metrics(tup):
    return pd.Series([fuzz.ratio(*tup),
                      fuzz.token_sort_ratio(*tup)],
                     ['ratio', 'token'])

fuzzyresults = compare.apply(metrics).unstack(0).idxmax().unstack(0)
fuzzyresults.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\10-Web-Scrapping\jobDB\fuzzy.csv',encoding='utf-8-sig')