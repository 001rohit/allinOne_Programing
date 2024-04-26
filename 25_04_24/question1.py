# Find the Largest Number in a List: Write a Python function to find the largest number in a list of numbers.

lst1 = [5,7,6,2,3,4,1]
largest=lst1[0]

for i in range(0,len(lst1)):
    if lst1[i]>largest:
        largest = lst1[i]

print(largest)