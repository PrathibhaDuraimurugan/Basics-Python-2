#Find the Factorial of a Number
#Using for Loop

num = int(input("Enter a number here: "))
fact = 1
if num < 0:
    print("Factorial of 0 does not exist")
if num == 0:
    print ("Factorial of 0 is", 1)
if num > 0:
    for i in range (1, num+1):
        fact = fact * i
print ("The factorial of the given number is", fact)

#Using recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
num = int(input("enter a number here: " ))
result = fact(num)
print ("The factorial of the given number is", result)