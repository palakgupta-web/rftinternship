# Data filtering tool
import pandas as pd
data={"NAME":["JYOTI","RAHUL","RIYA","SNEHA","ROHIT"],
        "SALARY":[50000,30000,60000,55000,40000],
        "AGE":[23,24,37,12,19]}
df=pd.DataFrame(data)
print("DATASET IS:\n")
print(df)
#Filter (salary>50000 and age <30)
filtered_results=df[(df["SALARY"]>50000) & (df["AGE"]<30)]
print("filtered results :\n",filtered_results)
# Save filtered data to new file
filtered_results.to_csv("filtered.csv",index=False) 
print("filtered data is saved into filtered.csv.")