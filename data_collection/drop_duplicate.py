# Importing modules
import pandas as pd
import numpy as np 
import re 
import matplotlib.pyplot as plt 
file =r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection\data_collected(with_keywords).csv'

# Above is the path of csv file. 
df = pd.read_csv(file,encoding="cp1252") # The file format is cp1252
df.columns = ['id' , 'id','tweets','keywords']

# Drop duplicated values
df = df.drop_duplicates(["tweets"], keep = "last")
print(df.head)
df.to_csv('dropped_duplicates.csv')