import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Return the value of "y":

print(myvar["y"])   

# Create a simple Pandas Series from a dictionary:

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print("only series keys from dictionary:", myvar.keys())
print("only series keys from dictionary:", myvar.index)

print("Create a simple Pandas Series from a dictionary:", myvar)

# Create a Series using only data from "day1" and "day2":
myvar = pd.Series(calories, index = ["day1", "day2"])

print("Create a Series using only data from 'day1' and 'day':", myvar)
