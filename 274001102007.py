'''
274001102007
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R. Check if inserting the string R at the beginning or the end would convert the string S into a palindrome. 
'''
S, R = input().split()
if (S+R)[::-1] == S+R : 
    print(S+R)
elif (R+S)[::-1] == R+S : 
    print(R+S)
else:
    print(False)

