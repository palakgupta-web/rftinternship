import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")
print(df.head())

df["Date"] = pd.to_datetime(df["Date"])

#Average Temperature by City
avg_temp = df.groupby("City")["Temperature_C"].mean()
print(avg_temp)

#Hottest and Coldest City
hottest_city = avg_temp.idxmax()
hottest_temp = avg_temp.max()

coldest_city = avg_temp.idxmin()
coldest_temp = avg_temp.min()
print("\nHottest City:")
print(hottest_city, hottest_temp, "°C")
print("\nColdest City:")
print(coldest_city, coldest_temp, "°C")

#Rainy and Sunny Days Count
rainy_days = (df["Weather"] == "Rainy").sum()
sunny_days = (df["Weather"] == "Sunny").sum()
print("\nRainy Days:", rainy_days)
print("Sunny Days:", sunny_days)

#Temperature Trend
daily_temp = df.groupby("Date")["Temperature_C"].mean()
plt.figure(figsize=(10, 5))
plt.plot(
    daily_temp.index,
    daily_temp.values,
    marker="o"
)
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Weather Distribution
weather_count = df["Weather"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    weather_count.values,
    labels=weather_count.index,
    autopct="%1.1f%%"
)
plt.title("Weather Distribution")
plt.show()

#Average Temperature per City
plt.figure(figsize=(8, 5))
plt.bar(
    avg_temp.index,
    avg_temp.values
)
plt.title("Average Temperature per City")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()

#Tomorrow's Temperature
temperature = df["Temperature_C"]
moving_average = temperature.rolling(window=3).mean()
tomorrow_temperature = moving_average.iloc[-1]
print("\nPredicted Temperature for Tomorrow:")
print(round(tomorrow_temperature, 2), "°C")

#Create Final Report
report = pd.DataFrame({
    "City": avg_temp.index,
    "Average_Temperature_C": avg_temp.values
})
report["Hottest_City"] = hottest_city
report["Hottest_Temperature_C"] = hottest_temp
report["Coldest_City"] = coldest_city
report["Coldest_Temperature_C"] = coldest_temp
report["Rainy_Days"] = rainy_days
report["Sunny_Days"] = sunny_days
report["Tomorrow_Predicted_Temperature_C"] = round(
    tomorrow_temperature, 2
)
report.to_csv("weather_final_report.csv",index= False)

#Dashboard
st.title("Weather Dashboard")

df = pd.read_csv("weather_data.csv")
st.dataframe(df)

# Average temperature
avg = df.groupby("City")["Temperature_C"].mean()

st.subheader("Average Temperature")
st.bar_chart(avg)

# Weather distribution
st.subheader("Weather Distribution")
st.bar_chart(df["Weather"].value_counts())

# Hottest & Coldest
st.write("Hottest City:", avg.idxmax())
st.write("Coldest City:", avg.idxmin())

# Rainy & Sunny days
st.write("Rainy Days:", (df["Weather"] == "Rainy").sum())
st.write("Sunny Days:", (df["Weather"] == "Sunny").sum())

# Prediction
prediction = df["Temperature_C"].rolling(3).mean().iloc[-1]
st.write(f"Tomorrow's Temperature: {prediction:.2f} °C")