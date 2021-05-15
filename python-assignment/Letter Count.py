"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
1.takes a sentence from the user,
2.counts the number of each letter of the sentence,
3.collects the letters/chars as a key and the counted numbers as a value in a dictionary.
Sample inputs	=  hippo runs to us!	
Outputs = {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 
'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}
"""

letter_count = list(str(input("Enter your sentences:")))
unique_word = set(letter_count)
final_dict = {}
for i in unique_word :
    time = letter_count.count(i)
    final_dict.update({i:time})
print(final_dict)







