import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("employee.csv")

print(df.head())

#department wise average performance
avg_performance = df.groupby("Department")["Performance_Score"].mean()
print(avg_performance)

#top 10 performers
top10 = (df.groupby("Employee_Name")["Performance_Score"].sum().sort_values(ascending=False).head(10))
print(top10)

#Employees attendance below 75%
print(df[df["Attendance_Percentage"]<75.0])

#Performance comparison chart
performance= df.groupby("Employee_ID")["Performance_Score"].sum()
plt.figure(figsize=(100,50))
plt.bar(performance.index,performance.values)
plt.xlabel("Employee ID")
plt.ylabel("score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Attendance trend
attendance= df.groupby("Employee_ID")["Attendance_Percentage"].sum()
plt.figure(figsize=(50,20))
plt.plot(performance.index,performance.values)
plt.xlabel("Employee ID")
plt.ylabel("attendance percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Department distribution
department_distribution = df.groupby("Department")["Performance_Score"].sum()
plt.pie(department_distribution.values,labels=department_distribution.index, autopct = "%1.1f%%")
plt.legend()
plt.show()

#export final report
df.to_csv("clean_employee.csv")

#dashboard
st.title("Employee Performance Analytics Dashboard")

df = pd.read_csv("employee.csv")

st.subheader("Employee Data")
st.dataframe(df)

st.subheader("Department-wise Performance")

department_avg = df.groupby("Department")["Performance_Score"].mean()

st.bar_chart(department_avg)

st.subheader("Attendance")

attendance = df.groupby("Employee_ID")["Attendance_Percentage"].mean()

st.line_chart(attendance)

st.subheader("Top 10 Performers")

top10 = (
    df.groupby("Employee_Name")["Performance_Score"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top10)

st.subheader("Employees with Attendance Below 75%")

low_attendance = df[df["Attendance_Percentage"] < 75]

st.dataframe(low_attendance)