# Student performance dashboard
import matplotlib.pyplot as plt
import numpy as np
# Dataset
students=["AMIT","RIYA","JOHN"]
subjects=["MATH","SCIENCE","ENGLISH"]
amit_marks=[85,78,90]
riya_marks=[92,88,85]
john_marks=[78,82,74]
# Grouped Bar chart
x=np.arange(len(subjects))
width=0.25
plt.bar(x-width, amit_marks,width,label="Amit",color="green")
plt.bar(x, riya_marks,width,label="Riya",color="red")
plt.bar(x+width, john_marks,width,label="John",color="blue")
plt.title("Student performance dashboard")
plt.xlabel("Students")
plt.ylabel("marks")
plt.xticks(x, subjects)
plt.legend()
plt.show()