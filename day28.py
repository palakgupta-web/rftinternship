import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
df = pd.read_csv("stock_market.csv")

print(df.head())

df["Investment"] = df["Buy_Price"] * df["Quantity"]


# Calculate Profit / Loss

df["Profit_Loss"] = (
    (df["Sell_Price"] - df["Buy_Price"])
    * df["Quantity"]
)

print(df[["Stock", "Profit_Loss"]].head())


# Profit/Loss for Each Stock
stock_performance = (
    df.groupby("Stock")["Profit_Loss"]
    .sum()
    .sort_values(ascending=False)
)

print(stock_performance)


# Best Performing Stock

best_stock = stock_performance.idxmax()
best_profit = stock_performance.max()

print("\nBest Performing Stock:", best_stock)
print("Profit:", best_profit)

# Worst Performing Stock

worst_stock = stock_performance.idxmin()
worst_loss = stock_performance.min()

print("\nWorst Performing Stock:", worst_stock)
print("Profit/Loss:", worst_loss)

# Overall Portfolio Return

total_investment = df["Investment"].sum()
total_profit = df["Profit_Loss"].sum()

portfolio_return = (
    total_profit / total_investment
) * 100

print("\nTotal Investment:", total_investment)
print("Total Profit/Loss:", total_profit)
print("Overall Portfolio Return:", portfolio_return, "%")


# Portfolio Growth Chart


daily_portfolio = (
    df.groupby("Date")["Investment"]
    .sum()
)

plt.figure(figsize=(10, 5))

plt.plot(
    daily_portfolio.index,
    daily_portfolio.values,
    marker="o"
)

plt.title("Portfolio Growth")
plt.xlabel("Date")
plt.ylabel("Investment")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Sector-wise Investment


sector_investment = (
    df.groupby("Sector")["Investment"]
    .sum()
)

print("\nSector-wise Investment:")
print(sector_investment)

plt.figure(figsize=(7, 5))

plt.bar(
    sector_investment.index,
    sector_investment.values
)

plt.title("Sector-wise Investment")
plt.xlabel("Sector")
plt.ylabel("Investment")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Daily Return Analysis


daily_profit = (
    df.groupby("Date")["Profit_Loss"]
    .sum()
)

daily_investment = (
    df.groupby("Date")["Investment"]
    .sum()
)

daily_return = (
    daily_profit / daily_investment
) * 100

print("\nDaily Return:")
print(daily_return)

plt.figure(figsize=(10, 5))

plt.plot(
    daily_return.index,
    daily_return.values,
    marker="o"
)


plt.title("Daily Return Analysis")
plt.xlabel("Date")
plt.ylabel("Return (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Moving Average
# Calculate average Sell Price for each day

daily_price = (
    df.groupby("Date")["Sell_Price"]
    .mean()
)

daily_price = daily_price.sort_index()

daily_price_df = pd.DataFrame({
    "Price": daily_price
})

daily_price_df["Moving_Average"] = (
    daily_price_df["Price"]
    .rolling(window=3)
    .mean()
)

print("\nMoving Average:")
print(daily_price_df)


# 12. Predict Next Day Trend

last_price = daily_price_df["Price"].iloc[-1]
last_ma = daily_price_df["Moving_Average"].iloc[-1]

print("\nNext Day Trend Prediction:")

if last_price > last_ma:
    print("Possible UPWARD / BULLISH trend")
elif last_price < last_ma:
    print("Possible DOWNWARD / BEARISH trend")
else:
    print("Possible SIDEWAYS trend")


df = pd.read_csv("stock_market.csv")

# Calculations
df["Investment"] = df["Buy_Price"] * df["Quantity"]

df["Profit_Loss"] = (
    (df["Sell_Price"] - df["Buy_Price"])
    * df["Quantity"]
)

df["Current_Value"] = (
    df["Sell_Price"] * df["Quantity"]
)

# Title
st.title("📈 Stock Portfolio Analyzer")

# KPIs
total_investment = df["Investment"].sum()
total_profit = df["Profit_Loss"].sum()

portfolio_return = (
    total_profit / total_investment
) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Investment", f"₹{total_investment:,.0f}")
col2.metric("Profit/Loss", f"₹{total_profit:,.0f}")
col3.metric("Return", f"{portfolio_return:.2f}%")

# Stock Performance
st.subheader("📊 Stock Performance")

stock_profit = df.groupby("Stock")["Profit_Loss"].sum()

st.bar_chart(stock_profit)

# Sector Investment
st.subheader("🏢 Sector-wise Investment")

sector = df.groupby("Sector")["Investment"].sum()

st.bar_chart(sector)

# Portfolio Growth
st.subheader("📈 Portfolio Growth")

growth = df.groupby("Date")["Current_Value"].sum()

st.line_chart(growth)

