import json
import csv
import pandas as pd

# Read json file and then write that on the csv file.
with open('data_update.json', 'r', encoding = 'utf-8') as input_file:
    data = json.load(input_file)

csv_data = data["data"]
#print(csv_data)
# Open a file for writing
csv_file = open('data_file.csv','w')
# create the csv writer object
csv_writer = csv.writer(csv_file)

# Counter variable used for writing 
# headers to the csv file 
count = 0 

for tweet in csv_data:
    if count == 0 :
        header = tweet.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(tweet.values())
csv_file.close()

# Queries - nuclear power , nuclear energy, nuclear reactors, nuclear fission, nuclear waste
# nuclear safety, nuclear fuel        