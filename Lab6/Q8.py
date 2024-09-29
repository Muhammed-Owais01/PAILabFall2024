import pandas as pd

pDf = pd.read_csv('Lab6/products.csv')
oDf = pd.read_csv('Lab6/orders.csv')

joined_df = pd.merge(pDf, oDf, how='inner', on='ProductID')
joined_df["Revenue"] = joined_df["Price"] * joined_df["Quantity"]
joined_df['OrderDate'] = pd.to_datetime(joined_df['OrderDate'], format='%m-%d-%Y')
highest_revenue_row = joined_df.loc[joined_df['Revenue'].idxmax()]


joined_df['Year'] = joined_df['OrderDate'].dt.year
joined_df['Month'] = joined_df['OrderDate'].dt.month

monthly_revenue = joined_df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

monthly_revenue.columns = ['Year', 'Month', 'Total Revenue']

joined_df = joined_df.dropna(subset=['ProductID', 'ProductName', 'OrderID', 'Quantity'])
joined_df['Price'] = pd.to_numeric(joined_df['Price'], errors='coerce')
joined_df = joined_df.dropna(subset=['Price'])


print("First 5 Products: \n", pDf.head(5))
print("First 5 Orders: \n", oDf.head(5))
print("Last 10 Products: \n", pDf.tail(10))
print("Last 10 Orders: \n", oDf.tail(10))
print("Total Revenue From Orders: \n", joined_df["Revenue"].sum())
print("Top 5 Best Selling Products: \n", joined_df["Revenue"].nlargest(5))
print("Top 5 Low Selling Products: \n", joined_df["Revenue"].nsmallest(5))
print("Top 5 Best Selling Products Common: \n", joined_df["Revenue"].nlargest(5).mode())
print("Average of Products of Each Category: \n", pDf.groupby('Category')['Price'].mean())
print("Day of Highest Revenue: ", highest_revenue_row["OrderDate"].day, "Month: ", highest_revenue_row["OrderDate"].month, "Year: ", highest_revenue_row["OrderDate"].year)
print(monthly_revenue)

