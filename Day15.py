import pandas as pd
import matplotlib.pyplot as plt
# Dataset
data={"students":["Rahul","jyoti","Aman","Pooja","Mahak"],
        "marks":[92,87,78,50,99]}
df= pd.DataFrame(data)
plt.figure(figsize=(15,5))
# PIE CHART
plt.subplot(1,4,1)
plt.pie(df["marks"], labels= df["students"], autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")

# BAR CHART
plt.subplot(1,4,2)
plt.bar(df["students"],df["marks"],color='cyan')
plt.title("Bar chart")
plt.xlabel("students")
plt.ylabel("marks")

# LINE CHART
plt.subplot(1,4,3)
plt.plot(df["students"],df["marks"],marker="*",color="magenta",linewidth=2)
plt.title("Line Chart")
plt.xlabel("students")
plt.ylabel("marks")

# OUTLIER detection
plt.subplot(1,4,4)
plt.boxplot(df["marks"])
plt.title("outlier detection")
plt.ylabel("marks")

#dashboard title
plt.suptitle("Student marks mini EDA dashboard")
plt.show()

#Insights
print("INSIGHTS")
print("1. Mahak scored the highest marks.")
print("2. Pooja scored the lowest marks.")
print("3. Pooja's marks appeared as an outlier.")
print("4. Overall student performance is good.")