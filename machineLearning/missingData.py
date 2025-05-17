import pandas as pd

dataset = pd.read_csv(r"C:\Users\soubh\PycharmProjects\PythonProject\machineLearning\titanic_data.csv")

print(dataset.head(6))

# print(dataset.shape)
print(dataset.isnull())