# Customer segmentation analysis
import pandas as pd
import matplotlib.pyplot as plt
# Dataset
data={"customer_id":[91,92,93,94,95,96,97,98],
        "age":[22,35,28,29,45,40,50,36],
        "spending":[2000,3000,1500,3500,4500,4000,3000,5000],
        "visits":[5,12,7,20,10,25,4,15]}
df= pd.DataFrame(data)
# Group customer by spending level
def group_customer(spending):
    if spending>=4000:
        return "High"
    elif spending>=2000:
        return "Medium"
    else:
        return "Low"
df["category"]= df["spending"].apply(group_customer)
print("Customer data:\n",df)

# High value customer
high_value=df[df["category"]=="High"]
print("High value customer:\n",high_value)

# low engagement customer
low_engagement= df[df["visits"]<6]
print("Low engagement customer:\n",low_engagement)

# Spending distribution
plt.figure(figsize=(6,5))
plt.hist(df["spending"],bins=5,color="cyan",edgecolor="purple")
plt.title("customer spending distribution")
plt.xlabel("spending")
plt.ylabel("Number of customers")
plt.show()

# Customer categories
category_count= df['category'].value_counts()
plt.figure(figsize=(6,5))
plt.bar(category_count.index, category_count.values)
plt.title("customer catgories.")
plt.xlabel("category")
plt.ylabel("count")
plt.show()

# Business Strategies
print("Business Strategies")
print("1. Give special offer to hogh value customers.")
print("2. Improve engagement for low engagement customers.")
print("3. Provide discounts for medium customers to increase spending.")
print("4. Give membership benefits for frequent visitors.")
