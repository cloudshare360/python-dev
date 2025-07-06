

# Code by Studyopedia

import pandas as pd

# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print("Student Records \n\n", df);


## Access using rows or coumns by Integer Positions

print("\n value", df.iloc [[1,2]])

print("\n value", df.iloc [[0,1]])

