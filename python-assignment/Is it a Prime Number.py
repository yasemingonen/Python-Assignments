#Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

#The examples of the desired output are as follows :

#input →  19 ⇉ output : 19 is a prime number
#input →  10 ⇉ output : 10 is not a prime number

number = int(input("please enter a number: "))
abc = 0


for i in range(1, number+1) :
   if not number % i :
       abc += 1

if (number == 0) or (number == 1) or (abc >= 3) :
    print(number, "is not prime number")
else:
    print(number, "is a prime number")


