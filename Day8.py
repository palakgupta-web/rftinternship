#Employee salary insights
import pandas as pd
data={"NAME":["A","B","C","D"],
        "DEPT":["IT","HR","IT","HR"],
        "SALARY":[50000,40000,60000,45000]}
df= pd.DataFrame(data)
print(df)
# Average salary per department
average_salary= df.groupby("DEPT")["SALARY"].mean()
print("Average salary per department is:\n",average_salary)
# highest paid employee per department
highest_paid= df.loc[df.groupby("DEPT")["SALARY"].idxmax()]
print("highest paid employee per department:\n",highest_paid)
# count employees per department
count=df.groupby("DEPT")["NAME"].count()
print("Number of employees in each department:\n",count)
# sorting the departments by average salary
sorted_dept=average_salary.sort_values()
print("Sorting the department by average salary:\n",sorted_dept)