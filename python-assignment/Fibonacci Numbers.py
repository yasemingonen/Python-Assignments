#Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

#The desired output is like :

#fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
n = int(input("enter a number: "))
fibonacci_numbers = [0, 1]
for i in range(2,n):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(fibonacci_numbers)

    




