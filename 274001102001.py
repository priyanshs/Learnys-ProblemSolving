'''
274001102001
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given an alphanumeric string S of length greater than 5. You are tasked with creating new strings with a maximum of one character each. If the character is repeated more than once in S, the same should be done on its respective substring. 
'''

S = input()
Q = list()
for val in set(S): 
    Q.append(val*S.count(val))

Q.sort()
print(Q)