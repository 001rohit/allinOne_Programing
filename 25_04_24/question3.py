# Find the Third Largest Number in a List: Write a Python function to find the second largest number in a list of numbers.

list3 =[4,3,5,2,8,9]
first = list3[0]
second = list3[0]
third = list3[0]

for i in list3:
    if i >first:
        third = second
        second = first
        first = i
        temp = first
    elif  i>second and i!=first:
           third = second
           second =i
           temp1 = second
    elif i>third and i!=second:
         third = i

print(third)