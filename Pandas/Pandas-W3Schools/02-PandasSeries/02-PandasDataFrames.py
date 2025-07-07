

#DataFrames

'''
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
'''

# Create a DataFrame from two Series:

import pandas as pd
import os


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

calories_series = myvar["calories"]
print(calories_series)

# Get the "duration" Series
duration_series = myvar.duration
print(duration_series)

'''
#What is a DataFrame?
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with #rows and columns.
'''

# Create a simple Pandas DataFrame:

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

# Locate Row
# Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[2])  # Returns the row with index 2

#Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])

# Named Indexes
# With the index argument, you can name your own indexes.
# Add a list of names to give each row a name:

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).
#refer to the named index:
print(df.loc["day2"])

# Load Files Into a DataFrame# 
#If your data sets are stored in a file, Pandas can load them into a DataFrame.

#import pandas as pd

import pandas as pd

# Define base directory and file name
base_dir = os.getcwd()  # Current working directory [[6]]
print("Base Directory:", base_dir );
file_name = 'data.csv'

# Dynamically build the full file path


script_directory = os.path.dirname(os.path.abspath(__file__))

print("Script File Directory:", script_directory)

file_path = os.path.join(script_directory, file_name)
print(f"Attempting to load data from: {file_path}")

try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")