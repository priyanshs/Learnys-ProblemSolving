'''
274026092006
Decompress Strings 
Strings - 1
Easy (TCS NQT)
You shall be given an alphanumeric string as an input. The task at hand is to decompress the string. Each character is succeeded by a single digit numeric value. Your task is to create a new string such that you repeat the character according to the number presented. 

Note: The strings are case sensitive, and thus considerations should be made. 
'''
string = input()

empty = ""
for r in range(len(string)):
    if string[r].isnumeric() and r != 0: 
        empty += string[r-1] * (int(string[r]) - 1)
    else: 
        empty += string[r]
print(empty)

