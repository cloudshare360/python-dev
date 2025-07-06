


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


## use the index Arguments





