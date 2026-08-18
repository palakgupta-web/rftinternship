#Prime Number
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%2==0:
            return False
    return True
num= int(input("Enter a number:"))
if is_prime(num):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
# Function using *args to find largest
def find_largest(*args):
    return max(args)
print("Largest number using *args:",find_largest(10,50,33,98,76))

#Function using *kwargs for student info
def student_info(**kwargs):
    print("Student information:")
    for key,value in kwargs.items():
        print(key,":",value)
student_info(name="Jyoti",
        age= 20,
        branch="AIML",
        college="B.Tech",
        year="3rd year")
#Function returns maximum,minimum,average,sum
def number(numbers):
    maximum= max(numbers)
    minimum= min(numbers)
    addition=sum(numbers)
    average=addition/len(numbers)

    return maximum,minimum,addition,average
numbers=[44,68,75,12,34,77,90]

maximum,minimum,addition,average= number(numbers)
print("maximum number is:", maximum)
print("minimum number is:", minimum)
print("addition of numbers is:", addition)
print("Average of numbers is:", average)

