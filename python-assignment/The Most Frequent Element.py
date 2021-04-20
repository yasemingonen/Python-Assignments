# The Most Frequent Element
# Task: Find out the most frequent number and its frequency.
    #Write a program that;
    #Finds out the most frequent number in the given list.
    #Calculates its frequency.

numbers = [16, 0, 15, 5, 7, 8, 16, -10, 16, 88, 16]
text = "The most frequent number is {} and it was {} times repeated."

a = max(set(numbers), key=numbers.count)
b = numbers.count(max(set(numbers), key=numbers.count))
print(text.format(a, b))