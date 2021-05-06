#Task : Print the prime numbers which are between 1 to entered limit number (n).

#You can use a nested for loop.
#Collect all these numbers into a list
#The desired output for n=100 :

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
#61, 67, 71, 73, 79, 83, 89, 97]


not_prime = []
list_prime = []
number = input("enter a number:")
if number.isdecimal() == False or type(number) == float or int(number) <= 1 :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) > 1 :
    for i in range(2, int(number)+1) :
        for j in range(2, i) :
            if i % j == 0 :
                not_prime.append(i)
                break
        else :
            list_prime.append(i)
print(f"Prime number is : ", list_prime)
print(f"Not prime number is :", not_prime)





