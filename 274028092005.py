'''
274028092005
Title: Move substring 
Category: Strings - 2 
Difficulty: Easy (TCS NQT)
Statement: 
You are given two alphanumeric strings of length greater than 5, S and R. You are tasked with finding the string and moving the string to the end. If the string is not present print -1. Print the newly created string.
'''
def fun(S,R): 
    if R in S : 
        ind = S.index(R)
        return S[:ind] + S[ind+len(R):] + S[ind:ind+len(R)] 
    else: 
        return -1 
S = input()
R = input()
S, R = T 
print(fun(S,R))