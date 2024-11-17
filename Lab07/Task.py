import pandas as pd

df = pd.read_csv("heart.csv")
print(df[df["cp"] == 2])
df = df.rename(columns={"sex": "gender"})
df["gender"][df["gender"] == 1] = "Male"
df["gender"][df["gender"] == 0] = "Female"

# single g
df_gender = df.groupby("gender")

# single col
print(df_gender['chol'].max(), end='\n\n')
print(df_gender['chol'].median(), end='\n\n')
print(df_gender['chol'].mean(), end='\n\n')

print(df_gender[["restecg", "oldpeak", "chol"]].max(), end='\n\n')
print(df_gender[["restecg", "oldpeak", "chol"]].median(), end='\n\n')
print(df_gender[["restecg", "oldpeak", "chol"]].mean(), end='\n\n')

df = pd.read_csv("iris.csv")
df = df.drop(columns={"Id"})
print(df)
