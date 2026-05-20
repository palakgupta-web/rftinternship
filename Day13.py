import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Dataset
marks=[45,50,55,92,63,65,90,76]
# create dataframe
df=pd.DataFrame({"marks":marks})
sns.histplot(df["marks"],kde=True,color="cyan")
plt.title("Distribution of student marks.")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
# skewness
print("Skewness:",df["marks"].skew())