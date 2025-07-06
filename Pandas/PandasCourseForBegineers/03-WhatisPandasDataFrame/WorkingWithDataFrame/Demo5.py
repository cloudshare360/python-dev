



# Code by Studyopedia

import pandas as pd

# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])

print("Student Records \n\n", df);


## Iteration

print("\nDisplay only Coloumn")

for col in df:
    print(col)

sorted_df = df.sort_values(by='Marks', ascending=False)
print("Sorted by Marks (Descending):\n", sorted_df)

sorted_df = df.sort_values(by='Marks')
print("Sorted by Marks:\n", sorted_df)

# Step 1: Sort DataFrame by Rank (ascending)
sorted_df = df.sort_values(by='Rank', ascending=True)

# Step 2: Dynamically generate new index labels
new_index = [f"Student{i+1}" for i in range(len(sorted_df))]

# Step 3: Assign new index
sorted_df.index = new_index

print("\nDynamically Reassigned DataFrame based on Rank:")
print(sorted_df)



# Sort by Marks descending
sorted_df = df.sort_values(by='Marks', ascending=False)

# Reassign index labels
sorted_df.index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']

print("\nReassigned DataFrame based on Marks:")
print(sorted_df)

