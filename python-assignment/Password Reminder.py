#Task : Let's say; you left a message in the past that prints a password you need. 
# To see the password you wrote, you need to enter your name and the program should recognize you.
#Write a program that 

#Takes the first name from the user and compares it to yours,
#Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
#If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

password_name = "Yasemin Firdevs"
password = "Mantra-7"
b= "Yasemin"

a= str(input("Please enter a user name: "))
if a == password_name :
    print("The password is: ", password)
elif  a == b :
    print("You have to add one more name!")
    c= str(input("Try again!: "))
    print(c)
    if c == password_name :
        print("The password is: ", password)
    else :
        print("You are not user!!")
else : 
    print("You are not user!!")

