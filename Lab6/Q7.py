import pandas as pd

df = pd.read_excel('employee.xlsx')

print(df[df["Year"] == 2020])