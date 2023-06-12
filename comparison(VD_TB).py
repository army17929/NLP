import pandas as pd

# Read the dataset into a pandas dataframe.
df = pd.read_csv('comparison(VADER,TB).csv')
print(df.shape)

# Find cells with different values. 
different_cells = df[df['sentiment_VADER'] != df['sentiment_TextBlob']]

print(different_cells)