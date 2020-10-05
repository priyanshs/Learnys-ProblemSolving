'''
274028092004
Title: Move sections 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given an alphanumeric string of length greater than 5. You are tasked with creating a new string such that every third and fifth character present in the string is moved to the end. Print the newly created string on the standard I/O.
'''
string = input() 
l = len(string)
oth = ""
third = ""
if l >= 5: 
    for i in range(l): 
        if i % 3 == 0 and i % 5 == 0 : 
            third += string[i]
        elif i % 3 == 0: 
            third += string[i]
        elif i % 5 == 0: 
            third += string[i]
        else: 
            oth += string[i]
    print(oth+third)
else: 
    print("Invalid Input")