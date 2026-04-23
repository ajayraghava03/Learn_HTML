# import pandas as pd

# data = {
#     "Name": ["Ajay", "Ravi", "Kiran"],
#     "Marks": [85, 90, 78]
# }

# df = pd.DataFrame(data)

# print(df)

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.head(2))
print(df.describe())

plt.scatter(df["Name"], df["Marks"])
plt.plot(df["Name"], df["Marks"])
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()