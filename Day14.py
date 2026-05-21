# category breakdown
import matplotlib.pyplot as plt
# Dataset
categories=["Food","Travel","Shopping"]
expenses=[500,300,200]

# Highlight highest categories
explode=[0.1 if i == max(expenses) else 0 for i in expenses]
#colors
colors=["magenta","cyan","lightgreen"]

# pie chart
plt.pie(expenses, labels= categories, autopct="%1.1f%%", explode= explode,colors= colors, shadow= True)

#title
plt.title("Category breakdown")
plt.show()