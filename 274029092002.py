'''
274029092002
Title: The Last Word 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
Given a string s consisting of upper/lower-case alphabets and empty characters ' ', ‘*’, ‘#’, ‘&’, return the length of the last word (last word means the last appearing word if we loop from left to right) in the string. If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
'''

string = input()

string = string.replace(' ', ', ') 
string = string.replace('*', ', ') 
string = string.replace('#', ', ') 
string = string.replace('&', ', ') 
string = string.split(', ')
while '' in string: 
    string.remove('')
if len(string) > 1: 
    print(len(string[-1]))
else: 
    print("Invalid Input")
