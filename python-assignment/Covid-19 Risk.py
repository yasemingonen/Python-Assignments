#Task : Estimating the risk of death from coronavirus. Write a program that;
#Takes "Yes" or "No" from the user as an answer to the following questions :
#Are you a cigarette addict older than 75 years old? Variable → age
#Do you have a severe chronic disease? Variable → chronic
#Is your immune system too weak? Variable → immune
#Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables 
# in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).
#age =  # can be assigned only True/False
#chronic =  # can be assigned only True/False
#immune =  # can be assigned only True/False
#risk = ?

age = str(input("Are you a cigarette addict older than 75 years old?(answer just yes or no): "))
chronic = str(input("Do you have a severe chronic disease?: "))
immune = str(input("Is your immune system too weak?: "))
if age == "no" and chronic == "no"  and immune == "no" :
    print("You are not in risky group") 
elif age != "yes" or "no" or chronic != "yes" or "no" or immune != "yes" or "no" :
    print("Please just write yes or no!") 
else :
    print("You are in risky group")