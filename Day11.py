# Sales Trend Visualization
import matplotlib.pyplot as plt
# Dataset
dates=["MON","TUE","WED","THU","FRI"]
sales=[200,250,300,280,350]
# plotting line chart
plt.plot(dates,sales,marker='*',linewidth=2)
# Highlight highest and lowest day
highest_day= dates[sales.index(max(sales))]
lowest_day=dates[sales.index(min(sales))]
plt.scatter(highest_day,max(sales),label="highest day")
plt.scatter(lowest_day,min(sales),label="lowest day")
# adding the title
plt.title("Sales Trend Visualization")
# adding the Labels
plt.xlabel("Dates")
plt.ylabel("Sales")
plt.legend()
plt.show()