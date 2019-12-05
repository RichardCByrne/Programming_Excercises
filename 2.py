'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320'''


### Method 1 ###
# Use for loop for continuous checking
# Define number


# n = int(input("Enter a whole number: "))
# fact = 1

# for num in range(1, n+1):
#    fact = fact * num


# print("The factorial of " + str(n) + " is:" + (str(fact)))




### Method 2 ###
# import math

# print(math.factorial(int(input("Enter a whole number: "))))




### Method 3 ###
#num = int(input("Enter a number: "))

#def fact(num):
#    if num == 0:
#        return 1
#    else:
#        return num * fact(num - 1)
#
#print(fact(num))







num = int(input())

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

print(fact(num))








