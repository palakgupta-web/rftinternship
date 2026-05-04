data=[10,None,20,10,"",30,None,40]
clean_list=[]

# Remove duplicacy and invalid values (None,"") from list
for i in data:
    if (i not in clean_list and i != None and i != "") :
        clean_list.append(i)


# Print clean and sorted list
print("Clean and Sorted list:",clean_list)

# Number of removed values 
count=len(data)-len(clean_list)
print("Number of removed values:",count)