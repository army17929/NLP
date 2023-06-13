import pandas as pd

df = pd.read_csv(r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection\data_collected(with_keywords).csv',encoding='cp1252')
print(df.shape)

# Define the ranges and corresponding values
s = 3550 # This is the starting index.
i = 100 # This is the interval.

ranges = [(s, s+100, 'nuclear radiation'),(s+100,s+199,'nuclear raioactive'),(s+199,s+299,'nuclear power plant'),(s+299,s+399,'nuclear plant safety')
          ,(s+399,s+499,'nuclear IAEA'),(s+499,s+598,'nuclear power carbon'),(s+598,s+623,'nuclear energy greenhouse'),
          (s+623,s+640,'nuclear TMI'),(s+640,s+740,'nuclear incident'),(s+740,s+840,'nuclear plant accident'),
          (s+840,s+865,'nuclear energy greenhouse'),(s+865,s+965,'nuclear power security'),(s+965,s+1065,'nuclear energy policy')
          ,(s+1065,s+1165,'nuclear energy France'),(s+1165,s+1265,'nuclear energy solar'),(s+1265,s+1365,'nuclear energy hydro'),
          (s+1365,s+1465,'nuclear waste'),(s+1465,s+1565,'nuclear energy crisis'),(s+1565,s+1665,'nuclear spent fuel'),
          (s+1665,s+1684,'nuclear power positive'),(s+1684,s+1784,'nuclear power risk'),(s+1784,s+1884,'nuclear power debate'),
          (s+1884,s+1984,'nuclear power international'),(s+1984,s+2017,'nuclear power sustainability'),(s+2017,s+2044,'nuclear power public opinion'),
          (s+2044,s+2144,'nuclear power capacity'),(s+2144,s+2244,'nuclear power climate'),(s+2244,s+2344,'nuclear energy climate'),
          (s+2344,s+2444,'nuclear radioactive'),(s+2444,s+2544,'nuclear power radiation'),(s+2544,s+2643,'nuclear energy public')
          ,(s+2634,s+2734,'nuclear power public'),(s+2734,s+2813,'nuclear plant public'),(s+2813,s+2881,'nuclear fusion technology'),
          (s+2881,s+2943,'nuclear energy efficiency'),(s+2943,s+3043,'nuclear power future'),(s+3043,s+3143,'nuclear energy future'),
          (s+3143,s+3243,'nuclear power electricity'),(s+3243,s+3343,'nuclear energy electricity'),(s+3343,s+3443,'nuclear energy grid'),
          (s+3443,s+3543,'nuclear power grid'),(s+3543,s+3643,'nuclear reactor'),(s+3643,s+3743,'nuclear power environment'),
          (s+3743,s+3843,'nuclear energy environemnt'),(s+3843,s+3943,'nuclear power world'),(s+3943,s+4043,'nuclear power Europe'),
          (s+4043,s+4143,'nuclear energy Europe')]

# Fill the specified ranges in the column with the corresponding values
column_name = 'keywords'
for start, end, value in ranges:
    df.loc[start:end, column_name] = value

df.to_csv('updated_file.csv')