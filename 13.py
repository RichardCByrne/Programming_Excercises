''''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''



s = input()
nums = []
lett = []

for i in s:
    if i.isdigit():
        nums.append(i)

    elif i.isalpha():
        lett.append(i)

nums = len(nums)
lett = len(lett)

print("Letters " + str(lett))
print("Numbers " + str(nums))