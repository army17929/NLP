# Importing modules
import pandas as pd
import numpy as np 
import re 
import matplotlib.pyplot as plt 
import chardet 
import os

file =r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\updated_file.csv'
print(chardet.detect(file.encode()))

# Above is the path of csv file. 
df = pd.read_csv(file,encoding="cp1252", error_bad_lines = False) 
df.columns = ['no','id_numbers','id','tweets','keywords']
print(df.shape)

# Drop duplicated values
os.chdir(r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection')
df = df.drop_duplicates(["tweets"], keep = "last")
print(df.shape)
df.to_csv('Tweet_updated.csv')