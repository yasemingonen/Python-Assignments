# Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.
# A comfortable word is a word which you can type always alternating the hand you type with 
# (assuming you type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program which returns True if it's a comfortable word or False otherwise.

word = set(input("enter a word: "))
left = set("qwertasdfzxcvb")
right = set("yuiopjklmn")

leftcheck = bool(word.intersection(left))
rightcheck = bool(word.intersection(right))

if leftcheck and rightcheck :
    True
    print("It is comfortable word!")
else :
    print("It isn't comfortable word!")