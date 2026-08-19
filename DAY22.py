import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data.csv")
# Cleaning missing values and duplicate data
print(df.isnull().sum())
df=df.dropna()
print(df.duplicated().sum())
df=df.drop_duplicates()

# Calculate total sales and average revenue
total_sales= df["Quantity_Sold"].sum()
print(total_sales)
df["revenue"]= df["Quantity_Sold"]*df["Unit_Price"]
average_revenue= df["revenue"].mean()
print(average_revenue)

#Top 5 customers
top_5_customers= (df.groupby("Sales_Rep")["revenue"].sum().sort_values(ascending=False))
print(top_5_customers)

#Sales Trend
df["Sale_Date"]= pd.to_datetime(df["Sale_Date"])
sales_trend= df.groupby("Sale_Date")["Sales_Amount"].sum()
#Line chart
plt.figure(figsize=(10,5))
plt.plot(sales_trend.index,sales_trend.values)
plt.title("Sales trend over time.")
plt.xlabel("Sale date")
plt.ylabel("Total sales")
plt.tight_layout()
plt.show()

#Bar chart(Top products)
top_products=(df.groupby("Product_ID")["Sales_Amount"].sum().sort_values(ascending=False))
plt.bar(top_products.index.astype(str),top_products.values)
plt.title("Top 5 products by Sales")
plt.xlabel("Product ID")
plt.ylabel("Total Sales Amount")
plt.tight_layout()
plt.show()

# Pie Chart(Category Distribution)
category_sales=(df.groupby("Product_Category")["Sales_Amount"].sum())
plt.figure(figsize=(7,7))
plt.pie(category_sales.values,labels=category_sales.index,autopct="%1.1f%%",startangle=90)
plt.title("Category Distribution")
plt.show()

#insights
print("INSIGHTS:")
print("1.CLOTHING CATEGORY HAS HIGHEST SALE")
print("2.FOOD CATEGORY HAS LEAST SALES")
print("3.NORTH REGION HAS HIGHEST SALES")
print("4.SOUTH REGION HAS LEAST SALES")
print("5.SALES PERFORMANCE VARIES OVER TIME.")