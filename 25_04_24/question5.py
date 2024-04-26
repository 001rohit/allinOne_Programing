# Count the Occurrences of an Element in a List: Write a Python function to count the number of occurrences of a specific element in a list.

list5 = [1,2,3,2,3,4,5,6,3,4,3]
num=3
count=0
for i in range(0,len(list5)):
    if(list5[i]==num):
         count+=1

print(count)