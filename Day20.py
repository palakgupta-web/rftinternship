import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("sales_data.csv")

# Data cleaning
print(df.isnull().sum())
df.drop(columns=["Region_and_Sales_Rep"],inplace=True)

# Convert date column
df["Sale_Date"]= pd.to_datetime(df["Sale_Date"])
print("Cleaned dataset:\n",df)

# Analysis
print("Total sales:",df["Sales_Amount"].sum())
print("Total quantiy sold:",df["Quantity_Sold"].sum())

#Region-wise sale
region_sales= df.groupby("Region")["Sales_Amount"].sum()
print("Regionwise sales :\n",region_sales)

# Top sold category
top_sold= df.groupby("Product_Category")["Sales_Amount"].sum()
print("Top sold category:",top_sold.idxmax())

# Visualization
# Top sold category
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
top_sold.plot(kind="pie",autopct="%1.1f%%")
plt.title("Top sold category")
plt.legend()

# Region-wise sale
plt.subplot(1,2,2)
region_sales.plot(kind="bar",color="cyan")
plt.title(" Region wise sales")
plt.xlabel("region")
plt.ylabel("Sales amount")
plt.tight_layout()
plt.show()

#Insights
print("Insights are:")
print("1.Category clothing has highest sale.")
print("2.North region has highest sale.")
print("3.South region has least sale.")
print("4.Category food has least sale.")
