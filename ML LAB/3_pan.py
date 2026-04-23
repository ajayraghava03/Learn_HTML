import pandas as pd

# create data
data = {'Name': ['A', 'B', 'C'],
        'Marks': [90, 85, 88]}

df = pd.DataFrame(data)

print("Data:\n", df)

print("First rows:\n", df.head())

print("Info:\n")
df.info()

print("Summary:\n", df.describe())