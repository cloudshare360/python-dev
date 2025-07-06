

# Code by Studyopedia

import pandas as pd

# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 2, 3, 4, 5],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print("Student Records \n\n", df);

print("\nValue1\n", df.loc['RowA',  'Student']);
print("\nValue2\n", df.loc[['RowA'],  'Student']);
print("\nValue3\n", df.loc[['RowA', 'RowB', 'RowC'], 'Student']);





