
# Code by Studyopedia

import pandas as pd

# Dataset
data = {
    'student': ["Amit", "John", "Jacob", "David", "Steve"],
    'rank': [1, 2, 3, 4, 5],
    'marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data)

print("Student Records\n\n", df)