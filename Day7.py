#Student preformance dashboard
import pandas as pd
data={"NAME":["AMIT","RIYA","JOHN"],
    "MATH":[80,90,60],
    "SCIENCE":[70,88,65],
    "ENGLISH":[85,92,70]}
df=pd.DataFrame(data)
# average marks per student
df['AVERAGE']= (df["MATH"]+df["SCIENCE"]+df["ENGLISH"])/3
avg= df.groupby('NAME')['AVERAGE'].mean()
print("average marks per students:\n",avg)
# topper
topper=avg.idxmax()
print("topper :",topper)
# count student above average
overall_average=df['AVERAGE'].mean()
print("overall average is:",overall_average)
count= len(df[df['AVERAGE']>overall_average])
print("number of students above average:",count)
#add grade column
def grade(avg):
    if avg>=90:
        return "A"
    elif avg >=80:
        return "B"
    elif avg >=70:
        return "C"
    else:
        return "FAIL"
df["GRADE"]= df['AVERAGE'].apply(grade)
print("grade column added:\n",df)
#Subjectwise average
subject_average=df[['MATH','SCIENCE','ENGLISH']].mean()
print("subjectwise average is:\n",subject_average)
    

