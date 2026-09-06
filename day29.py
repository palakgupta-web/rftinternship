import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Import Expense Data

df = pd.read_csv("expenses.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

#  Automatic Categorization
def categorize_expense(description):
    description = description.lower()

    if any(word in description for word in ["grocery", "restaurant", "food"]):
        return "Food"
    elif any(word in description for word in ["uber", "cab", "bus", "travel"]):
        return "Transport"
    elif any(word in description for word in ["shirt", "shoes", "shopping"]):
        return "Shopping"
    elif any(word in description for word in ["electricity", "mobile", "internet"]):
        return "Bills"
    elif any(word in description for word in ["movie", "concert", "entertainment"]):
        return "Entertainment"
    elif any(word in description for word in ["medicine", "medical"]):
        return "Healthcare"
    elif any(word in description for word in ["gym"]):
        return "Fitness"
    else:
        return "Other"


df["Category"] = df["Description"].apply(categorize_expense)


# 3. Monthly Expense Calculation

monthly_expenses = df.groupby("Month")["Amount"].sum()

print("\nMonthly Expenses:")
print(monthly_expenses)

# 4. Income
monthly_income = 50000

total_expenses = df["Amount"].sum()
total_income = monthly_income * df["Month"].nunique()
total_savings = total_income - total_expenses

print("\n----- Budget Summary -----")
print("Total Income:", total_income)
print("Total Expenses:", total_expenses)
print("Total Savings:", total_savings)

# 5. Highest Spending Category

category_expenses = df.groupby("Category")["Amount"].sum()

highest_category = category_expenses.idxmax()
highest_amount = category_expenses.max()

print("Highest Spending Category:", highest_category)
print("Amount Spent:", highest_amount)

# 6. Savings Rate
savings_rate = (total_savings / total_income) * 100

print("Savings Rate:", round(savings_rate, 2), "%")

# Budget Status

if savings_rate >= 20:
    print("Budget Status: Good 👍")
else:
    print("Budget Status: Needs Improvement ⚠️")

# 8. Spending by Category
plt.figure(figsize=(8, 5))
category_expenses.plot(kind="bar")

plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Spending Trend

plt.figure(figsize=(8, 5))
monthly_expenses.plot(kind="line", marker="o")

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.grid(True)
plt.tight_layout()
plt.show()


# Expense Prediction
monthly_data = monthly_expenses.reset_index()
monthly_data.columns = ["Month", "Expense"]

monthly_data["Predicted_Expense"] = (
    monthly_data["Expense"]
    .rolling(window=3, min_periods=1)
    .mean()
)

print("\nExpense Prediction:")
print(monthly_data)


# Export Final Report

df.to_csv("final_expense_report.csv", index=False)

monthly_data.to_csv(
    "monthly_budget_summary.csv",
    index=False
)

print("\nReports exported successfully!")

# PAGE CONFIG


st.set_page_config(
    page_title="Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Smart Expense Tracker & Budget Analyzer")
st.write("Track your expenses, analyze your budget and predict future spending.")


# LOAD DATA

df = pd.read_csv("expenses.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# AUTOMATIC CATEGORIZATION


def categorize_expense(description):

    description = description.lower()

    if any(word in description for word in
           ["grocery", "restaurant", "food", "dinner", "lunch"]):
        return "Food"

    elif any(word in description for word in
             ["uber", "cab", "bus", "travel"]):
        return "Transport"

    elif any(word in description for word in
             ["shirt", "shoes", "shopping"]):
        return "Shopping"

    elif any(word in description for word in
             ["electricity", "mobile", "internet", "recharge"]):
        return "Bills"

    elif any(word in description for word in
             ["movie", "concert"]):
        return "Entertainment"

    elif any(word in description for word in
             ["medicine", "medical"]):
        return "Healthcare"

    elif "gym" in description:
        return "Fitness"

    else:
        return "Other"


df["Category"] = df["Description"].apply(categorize_expense)

# INCOME

monthly_income = 50000

number_of_months = df["Month"].nunique()

total_income = monthly_income * number_of_months
total_expenses = df["Amount"].sum()
total_savings = total_income - total_expenses

savings_rate = (total_savings / total_income) * 100

# CATEGORY ANALYSIS

category_expenses = df.groupby("Category")["Amount"].sum()

highest_category = category_expenses.idxmax()

# DASHBOARD METRICS


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💵 Total Income",
    f"₹{total_income:,.0f}"
)

col2.metric(
    "💸 Total Expenses",
    f"₹{total_expenses:,.0f}"
)

col3.metric(
    "💰 Total Savings",
    f"₹{total_savings:,.0f}"
)

col4.metric(
    "📊 Savings Rate",
    f"{savings_rate:.2f}%"
)


st.divider()


# BUDGET SUMMARY


st.subheader("📋 Budget Summary")

if savings_rate >= 20:
    st.success("✅ Budget Status: Good")
else:
    st.warning("⚠️ Budget Status: Needs Improvement")

st.write(
    f"Highest Spending Category: **{highest_category}**"
)


# SPENDING BY CATEGORY


st.subheader("📊 Spending by Category")

fig1, ax1 = plt.subplots()

category_expenses.plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel("Category")
ax1.set_ylabel("Amount")
ax1.set_title("Category-wise Spending")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig1)


# MONTHLY SPENDING TREND

st.subheader("📈 Monthly Spending Trend")

monthly_expenses = df.groupby("Month")["Amount"].sum()

fig2, ax2 = plt.subplots()

monthly_expenses.plot(
    kind="line",
    marker="o",
    ax=ax2
)

ax2.set_xlabel("Month")
ax2.set_ylabel("Expense")
ax2.set_title("Monthly Expense Trend")

ax2.grid(True)

plt.tight_layout()

st.pyplot(fig2)


# EXPENSE PREDICTION


st.subheader("🔮 Expense Prediction")

monthly_data = monthly_expenses.reset_index()

monthly_data.columns = [
    "Month",
    "Expense"
]

monthly_data["Predicted Expense"] = (
    monthly_data["Expense"]
    .rolling(
        window=3,
        min_periods=1
    )
    .mean()
)

st.dataframe(
    monthly_data,
    use_container_width=True
)

# Next month prediction
next_month_prediction = monthly_data["Expense"].tail(3).mean()

st.metric(
    "🔮 Predicted Next Month Expense",
    f"₹{next_month_prediction:,.0f}"
)


# EXPENSE DATA

st.subheader("🧾 Expense Data")

st.dataframe(
    df,
    use_container_width=True
)

# DOWNLOAD REPORT

st.subheader("📥 Export Report")

csv_data = df.to_csv(index=False)

st.download_button(
    label="Download Final Expense Report",
    data=csv_data,
    file_name="final_expense_report.csv",
    mime="text/csv"
)

