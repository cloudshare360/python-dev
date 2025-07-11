# Learn Pandas

about is Pandas
- Pandas is a Python library.
- Pandas is used to analyze data.

## Pandas Introduction

### What is Pandas?
- Pandas is a Python library used for working with data sets.
- It has functions for 
    - analysing
    - cleanining
    - exploring
    - manipulating 
     
     for data
### why use Pandas?
- Pandas allows us to analyse big data and make conclusions based on statistical theories
- Pandas can clean messy data sets, and make then readable and relevant
- Relevant data is very important in data science

### What can Pandas do?
- Is there a correlation between two or more columns?
- What is average value?
- Max value?
- Min value?
- Pandas can delete rows that are not relevant or contain incorrect values.
- This includes rows with empty or NULL values.
- The process is known as cleaning the data.

The name 'Pandas' is short for one of the following: Pane; Data

## Pandas Getting Started

### installing Pandas
```
pip install pandas
```
### Validated if Pandas is installed
```
pip3 show pandas
```
```
python3 -c "import pandas; print(pandas.__version__)"
```
or

```
pip3 show pandas | grep Version
```

# Pandas Series
## What is a Series?

a pandas Series is like a column in a table
it is a one dimensional array holding data of any type

Create a simple Pandas Series from a list:

```
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

```