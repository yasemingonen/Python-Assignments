# Find the Missing Number
# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

missing_num1 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
missing_num2 = [7, 2, 3, 6, 5, 9, 1, 4, 8]
missing_num3 = [10, 5, 1, 2, 4, 6, 8, 3, 9]

num1 = sum(missing_num1)
num2 = sum(missing_num2)
num3 = sum(missing_num3)

print("The missing number is :", 55 - num1)
print("The missing number is :", 55 - num2)
print("The missing number is :", 55 - num3)