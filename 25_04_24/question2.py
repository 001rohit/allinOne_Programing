# Find the Second Largest Number in a List: Write a Python function to find the second largest number in a list of numbers.

list2 = [12,11,2,8,4,6,7,1]
firstLarg = list2[0]
secondLarg = list2[0]

for i in list2:
    if i>firstLarg:
          secondLarg = firstLarg
          firstLarg = i
          temp = firstLarg
    elif i>secondLarg and i!=firstLarg:
         secondLarg = i

print(secondLarg)