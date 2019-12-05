'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''



upperCase = []
lowerCase = []

string = str(input("Enter a phrase: "))

for let in string:
    if let.isupper():
        upperCase.append(let)
    elif let.islower():
        lowerCase.append(let)
    else:
        pass

upperCase = len(upperCase)
lowerCase = len(lowerCase)

print("Upper " + str(upperCase))
print("Lower " + str(lowerCase))