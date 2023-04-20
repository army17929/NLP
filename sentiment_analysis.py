# Problnem statement 
# Input : text data from sentiment 140 dataset 
# Output : sentiment classification

# Import necessrary libraries.
# utilities
import re # Regular expression match, search, findall
import numpy as np 
import pandas as pd

# Plotting
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt 

# NLTK
from nltk.stem import WordNetLemmatizer

# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# Importing the dataset.
location = r"C:\Users\every\OneDrive\NLP_project\Sentiment_analysis\archive\training.1600000.processed.noemoticon.csv"
dataset_columns = ['target','ids','date','flag','user','text'] # This will be the head of the columns
dataframe = pd.read_csv(location,names = dataset_columns, encoding='ISO-8859-1') # Names = columns

#dataframe = pd.concat([dataframe_positive,dataframe_negative]) # The command concatenate will connect two different dataframes.
#print(dataframe)
#print(dataframe.head()) # This is going to show us the first five rows of the dataframe.
#print(dataframe.columns)
#print(dataframe.info())
#print(np.sum(dataframe.isnull().any(axis=1))) # this is counting the missing value numbers for all columns. axis = 1 means column
#print(dataframe['target'].unique(), dataframe['target'].nunique()) # This will present how many unique values are in the column. 

# There are only 0 and 4.

# Plotting the distribution for dataset. 
ax = dataframe.groupby('target').count().plot(kind='bar',title = 'Distribution of data',legend=False) # whole dataframe is grouped by target, which is the label.
ax.set_xticklabels(['Negative','Positive'],rotation = 0)
text, sentiment = list(dataframe['text']), list(dataframe['target'])
sns.countplot(x='target',data = dataframe)
#plt.show()

# then, we can start the pre-processing of the dataset.
data = dataframe[['text','target']] # We will select the text and the target column from the whole dataset. 
data['target'] = data['target'].replace(4,1) # Currently, positive sentiment was labeled as 4, but we will replace it as 1 so that it is more intuitive. 
print(data['target'].unique()) # Check whether the replacement was done properly.

data_pos = data[data['target'] == 1]
data_neg = data[data['target'] == 0]

data_pos = data_pos.iloc[:int(20000)]
data_neg = data_neg.iloc[:int(20000)] # Selecting specific columns and rows from the dataframe.
dataset = pd.concat([data_pos,data_neg])

# Convert uppercase into the lowercase.
dataset['text'] = dataset['text'].str.lower()
print(dataset['text'].tail())

# Next, we define the stopwords list in English.
import spacy
import nltk
from spacy.lang.en.stop_words import STOP_WORDS 
# This module removes redundant words from the text.
stopwords = list(STOP_WORDS) # We can add or substract some of the words. 

def cleaning_stopwords(text) :
    return " ".join([word for word in str(text).split() if word not in stopwords])
    # This function will return the survived words from the input. 
dataset['text'] = dataset['text'].apply(lambda text : cleaning_stopwords(text)) # This line means that for all the elements in dataset[txt], the function will be applied.
print(dataset['text'].head())

# Cleaning and removing punctuations.
import string 
english_punctuations = string.punctuation
punctuation_list = english_punctuations

def cleaning_punctuations(text) :
    translator = str.maketrans('','',punctuation_list) # str is a converting function, like 'int' function.
    # Syntax of maketrans function is str.maketrans(x,y,z)
    # Where x is the original string. 
    # y is a string with same length of x. 
    # x[i] will be replaced to y[i].
    # z is an optional input, this is a string describing which characters to remove from the original string.
    # therefore, this function makes sense. x and y parameter have the same length and z is something that we should remove.
    return text.translate(translator)
dataset['text'] = dataset['text'].apply(lambda text: cleaning_punctuations(text))
print(dataset['text'].tail())

# Cleaning and removing repeating characters. 
def cleaning_repeating_char(text):
    return re.sub(r'(.)1+',r'1',text) # re.sub() function replaces certain string with another string.
# I think the second parameter should be '', not '1'?
    # Syntax : re.sub(x,y,z)
    # x is the string that should be replaced. 
    # y is the string that will substitute x. 
    # z is a set of strings. In this case it will be a sentence or a paragraph.
dataset['text'] = dataset['text'].apply(lambda text: cleaning_repeating_char(text))
print(dataset['text'].tail())