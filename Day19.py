#STOCK/TIME - SERIES ANALYSIS
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Stock": ["AAPL", "AAPL", "AAPL", "AAPL", "AAPL","GOOG", "GOOG", "GOOG", "GOOG", "GOOG"],
    "Price": [150, 152, 149, 155, 160,2800, 2820, 2790, 2850, 2900]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Stock", "Date"])

#moving average
df["moving"] = df.groupby("Stock")["Price"].transform(lambda x: x.rolling(3).mean())
print(df)

#peaks & drop
df["Prev"] = df.groupby("Stock")["Price"].shift(1)
df["Next"] = df.groupby("Stock")["Price"].shift(-1)

def detect_point(row):
    if pd.isnull(row["Prev"]) or pd.isna(row["Next"]):
        return "Neutral"
    
    if row["Price"] > row["Prev"] and row["Price"] > row["Next"]:
        return "Peak"
    elif row["Price"] < row["Prev"] and row["Price"] < row["Next"]:
        return "Drop"
    else:
        return "Normal"

df["Signal"] = df.apply(detect_point, axis=1)

print(df[["Date", "Stock", "Price", "Signal"]])

#VOLATILITY
df["Returns"] = df.groupby("Stock")["Price"].pct_change()
volatility = df.groupby("Stock")["Returns"].std()

print("\n Volatility (Risk Level):")
print(volatility)

#VISUALIZATION
plt.figure(figsize=(10, 5))

for stock in df["Stock"].unique():
    temp = df[df["Stock"] == stock]

    plt.plot(temp["Date"], temp["Price"], marker="o",label = "price")
    plt.plot(temp["Date"], temp["moving"], linestyle="--",label = "moving")

plt.title("Stock Price vs Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

#MULTI-STOCK COMPARISON
pivot = df.pivot(index="Date", columns="Stock", values="Price")
pivot.plot(figsize=(10, 5), marker="o")
plt.title("Stock Price Comparison")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid()
plt.show()