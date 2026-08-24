import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("transaction.csv")
df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

# Duplicates
print("Duplicates:", df.duplicated().sum())

# High value transactions
threshold = 100000
high_value = df[df["Amount"] > threshold]

# Suspicious accounts
count = df["Account_ID"].value_counts()
suspicious_accounts = count[count > 15].index
suspicious = df[df["Account_ID"].isin(suspicious_accounts)]

#transaction category chart 
category_count = df["Category"].value_counts() 
plt.bar(category_count.index , category_count.values) 
plt.title("Category Chart") 
plt.xlabel("category") 
plt.ylabel("count") 
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show() 

#daily transaction trend
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

transaction = df.groupby("Date")["Amount"].mean().reset_index()

fig, ax = plt.subplots()

ax.plot(transaction["Date"], transaction["Amount"], marker="o")

ax.set_title("Transaction Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Average Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 

#top 10 highest transaction 
top = df.groupby("Transaction_ID")["Amount"].sum() 
top_10 = top.sort_values(ascending=False) 
print(top_10) 

#suspicious transaction into seperate csv 
suspicious.to_csv( "suspicious_transaction.csv", index=False)

# Risk Score
df["Risk_Score"] = 0

df.loc[df["Amount"] > threshold, "Risk_Score"] += 40
df.loc[df["Account_ID"].isin(suspicious_accounts), "Risk_Score"] += 30

# Risk Level
df["Risk_Level"] = pd.cut(
    df["Risk_Score"],
    bins=[-1, 30, 60, 70],
    labels=["Low", "Medium", "High"]
)

# --------------------------------
# STREAMLIT DASHBOARD
# --------------------------------

st.title("💳 Fraud Detection Dashboard")

# Filters
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Category",
    df["Category"].unique()
)

risk = st.sidebar.multiselect(
    "Risk Level",
    df["Risk_Level"].dropna().unique()
)

search = st.sidebar.text_input("Search Account ID")

# Apply filters
filtered = df.copy()

if category:
    filtered = filtered[
        filtered["Category"].isin(category)
    ]

if risk:
    filtered = filtered[
        filtered["Risk_Level"].isin(risk)
    ]

if search:
    filtered = filtered[
        filtered["Account_ID"].str.contains(
            search, case=False, na=False
        )
    ]

# Metrics
st.metric("Total Transactions", len(filtered))

st.metric(
    "High Value Transactions",
    len(filtered[filtered["Amount"] > threshold])
)

st.metric(
    "High Risk Transactions",
    len(filtered[filtered["Risk_Level"] == "High"])
)

# Transaction data
st.subheader("Transaction Data")
st.dataframe(filtered)

# Category Chart
st.subheader("Transaction Category")

category_count = filtered["Category"].value_counts()

fig, ax = plt.subplots()
ax.bar(category_count.index, category_count.values)
ax.set_xlabel("Category")
ax.set_ylabel("Count")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)

# Daily Transaction Trend
st.subheader("Daily Transaction Trend")

daily = filtered.groupby("Date")["Amount"].mean()

fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
ax.set_xlabel("Date")
ax.set_ylabel("Average Amount")

st.pyplot(fig)

# Top 10 Transactions
st.subheader("Top 10 Highest Transactions")

top_10 = filtered.nlargest(10, "Amount")

st.dataframe(
    top_10[["Transaction_ID", "Account_ID", "Amount", "Risk_Level"]]
)

# Risk Distribution
st.subheader("Risk Level Distribution")

st.bar_chart(
    filtered["Risk_Level"].value_counts()
)

# Export suspicious transactions
suspicious.to_csv(
    "suspicious_transactions.csv",
    index=False
)