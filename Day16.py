import matplotlib.pyplot as plt
import pandas as pd
# Dataset
data={
    "DATE":["2025-05-01","2025-05-02","2025-05-03","2025-05-04","2025-05-05","2025-05-06","2025-05-07"],
    "PRODUCT":["shoes","Watch","Bag","Headphone","Shoes","Laptop","Watch"],
    "REGION":["Delhi","Mumbai","Chennai","Kolkata","Delhi","Mumbai","Pune"],
    "SALES":[15000,22000,None,18000,25000,55000,30000]
}
# create dataframe
df=pd.DataFrame(data)

# convert date column into datetime
df["DATE"]=pd.to_datetime(df["DATE"])

# handling missing value
df["SALES"].fillna(df["SALES"].mean(),inplace= True)
print("Dataset is:\n",df)

# total sales per product
total_sales=df.groupby("PRODUCT")["SALES"].sum()
print("Total sales per product :\n",total_sales)

# region-wise performance
region_sales=df.groupby("REGION")["SALES"].sum()
print('Region wise sales:\n',region_sales)

# monthly growth analysis
monthly_sales= df.groupby(df["DATE"].dt.month)["SALES"].sum()
print("Monthly sales:\n",monthly_sales)

# Best performing region
best_region=region_sales.idxmax()
print("Best performing region:\n",best_region)

# VISUALIZATION
# Line chart
plt.figure(figsize=(8,5))
plt.plot(df["DATE"],df["SALES"],marker="o",linestyle="--",color="purple")
plt.title("Sales trend analysis")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(7,5))
total_sales.plot(kind="bar")
plt.title("Top product by sales")
plt.xlabel("Products")
plt.ylabel("Total sales")
plt.xticks(rotation=0)
plt.show()

# Key insights
print("\nKey Insights")
print("1.Laptop generated the highest sales.")
print("2.Mumbai region showed strong performance.")
print("3.Missing sales values were filled using mean.")