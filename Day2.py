marks=[78,85,90,67,85,92,78]
#average of the list
total=0
for i in marks:
    total+=i
average=total/len(marks)
print("average is:",average)
#highest and lowest value in a list
highest=marks[0]
lowest=marks[0]
for i in marks:
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
print("highest is:",highest)
print("lowest is:",lowest)
# number of students scored above average
count=0
for i in marks:
    if i > average:
        count+=1
print("No. of student scored above average:",count)
#grade distribution
def grades(num):
    if num>=90:
        return "A"
    elif num >=80:
        return "B"
    elif num>=70:
        return "C"
    else:
        return "Fail"
print("Grades are:")
for i in marks:
    print(grades(i))
    

