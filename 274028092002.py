'''
274028092002
Title: Abbreviation
Category: Strings - 1
Difficulty: Medium (TCS NQT)
Statement: 
A string abbreviation is considered valid if the abbreviated string has at least 3 characters and maximum of 5 characters. In addition the abbreviated strings should contain alphabets in the same order as they are presented in the string to be tested. You are tasked with writing a function which checks if the abbreviation is correct and returns a boolean response. 
'''

string = raw_input().split()
counter1 = 0 
counter2 = 0 
flag = list()
while counter1 <= len(string[0]): 
    if  counter2 < len(string[1]) and string[0][counter1] == string[1][counter2]: 
        counter2 += 1
        flag.append(True)
    counter1 += 1
    
if flag.count(True) == len(string[1]): 
    print(True)
else:
    print(False)