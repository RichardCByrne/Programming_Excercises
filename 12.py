''''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''



values = []

for num in range(1000, 3001):
    nums = str(num)
    if (int(nums[0]) % 2 == 0) and (int(nums[1]) % 2 == 0) and (int(nums[2]) % 2 == 0) and (int(nums[3]) % 2 == 0):
        values.append(nums)

print(",".join(values))