#opening a csv file
file=open("students.csv","r")
#read lines of csv file
lines=file.readlines()
#create a dictionary
dict=[]
# store csv data in dictionary
for items in lines[1:]:
    name,age,marks=items.strip().split(",")
    student={"NAME":name,"AGE":int(age),"MARKS":int(marks)}
    dict.append(student)
#closing the file
file.close()
#print the dictionary 
print(dict)
# finding the average of marks 
total=0
for student in dict:
    total=total+student["MARKS"]
average= total/len(dict)
print("Average of marks is:",average)