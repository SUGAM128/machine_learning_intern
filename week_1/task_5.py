#basic libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


numbers = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", numbers)


print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))

print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))


#pandas

data = {
    "Name": ["Ram", "Hari", "Sita", "Gita"],
    "Marks": [75, 80, 65, 90]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)


print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())



# Cmatplot
names = ["Ram", "Hari", "Sita", "Gita"]
marks = [75, 80, 65, 90]


plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

#scikit_learn

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [20, 30, 40, 50, 60]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("\nPredicted marks for 6 hours:", prediction[0])
