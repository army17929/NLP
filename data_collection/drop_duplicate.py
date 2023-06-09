# Importing modules
import pandas as pd
import numpy as np 
import re 
import matplotlib.pyplot as plt 
import chardet 

file =r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection\data_collected.csv'
print(chardet.detect(file.encode()))

# Above is the path of csv file. 
df = pd.read_csv(file,encoding="utf-8", error_bad_lines = False) 
df.columns = ['id_numbers','id','tweets']
print(df.shape)

# Drop duplicated values
df = df.drop_duplicates(["tweets"], keep = "last")
print(df.shape)
df.to_csv('dropped_duplicates.csv')