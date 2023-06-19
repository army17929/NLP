import csv
import pandas as pd
import numpy as np 

def find_different_cells(csv_file):
    different_cells = []
    unanimous = []
    with open(csv_file, 'r', encoding='cp1252') as file:
        reader = csv.reader(file)
        rows = list(reader)  # CSV 파일의 모든 행을 읽어옴

        # 비교 로직을 3, 4, 5, 6 열에만 적용
        for i in range(1, len(rows)):  # For all the rows in the file,
            for j in [3, 4, 5]:  # 3, 4, 5, 6 열만 비교
                if not rows[i][j] == rows[i][j-1]:  # If the values are different from each other.
                    cell = {'row': i, 'column': j, 'value': rows[i][j]}
                    different_cells.append(cell)
                else : 
                    cell_1 = {'row': i, 'column': j, 'value': rows[i][j]}
                    unanimous.append(cell_1)  

    return different_cells, unanimous

csv_file_path = r"C:\Users\every\OneDrive\바탕 화면\Github\NLP\Manually labelled\Tweet_updated_comparison.csv"

# Classification
different_cells = find_different_cells(csv_file_path)[0]

# Result for the different cells
matrix_0 = np.array([[cell['row'], cell['column'], cell['value']] for cell in different_cells])
different_rows = np.unique(matrix_0[:,0]) # Printing the unique values of the column 

list_different = [] # This is an empty list for the storage. 
for string in different_rows:
    string = int(string) # Originally, this starts from the string, we can convert it to the integers.
    list_different.append(string)

list_different.sort(key=int) # Key argument is needed because by default, sort function sorts string.
sorted_rows = list_different
print(sorted_rows,len(sorted_rows))

unanimous_rows = [num for num in range(1,101) if num not in sorted_rows]
print(unanimous_rows, len(unanimous_rows)) # Those are unanimous