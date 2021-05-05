# FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#Print numbers from 1 to 100 inclusively following these instructions:

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.


list_word = []
for i in range(100) :
    if i % 15 == 0 :
        list_word.append("FizzBuzz")
    elif i % 5 == 0 :
        list_word.append("Buzz")
    elif i % 3 == 0 :
        list_word.append("Fizz")
    else :
        list_word.append(i)
print(list_word)


