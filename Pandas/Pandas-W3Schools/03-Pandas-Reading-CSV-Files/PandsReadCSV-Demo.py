#Read CSV Files
'''
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.
'''

#Load the CSV into a DataFrame:
import pandas as pd
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'data.csv')

df = pd.read_csv(file_path)

print(df.to_string()) 