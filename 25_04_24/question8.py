# Check if a List is Palindrome: Write a Python function to check if a list is a palindrome.

str = "nitin"
res =""
for i in range(len(str)-1,-1,-1):
    res+=str[i]
if(res ==str):
    print("This string is pallindrom")
else:
    print("This string is not pallindrom")