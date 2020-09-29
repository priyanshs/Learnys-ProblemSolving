'''
274028092001
Title: Distance between strings 
Category: Strings - 3
Difficulty: Easy (TCS NQT)
Statement: 
Each character in a string can be easily associated with an ASCII code. You have to write a function which reads two strings character by character and finds the distance between them. The function written should return the total difference as well as a tuple containing difference for each character. 
'''

string = input().split()
counter = -1
if len(string[0]) > len(string[1]): 
    counter = 1
elif len(string[0]) <= len(string[1]): 
    counter = 0
else: 
    counter = -1 
li = list()
for i in range(len(string[counter])): 
    li.append( (ord(string[0][i]) - ord(string[1][i])) )
for i in range(len(string[counter]), len(string[~counter+2]) ): 
    if ~counter+2 == 1: 
        li.append( -1 * ord(string[~counter+2][i]))
    else:
        li.append(ord(string[~counter+2][i]))
print(li, sum(li))