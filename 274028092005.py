'''
274028092005
Title: Move substring 
Category: Strings - 2 
Difficulty: Easy (TCS NQT)
Statement: 
You are given two alphanumeric strings of length greater than 5, S and R. You are tasked with finding the string and moving the string to the end. If the string is not present print -1. Print the newly created string.
'''
def fun(S,R): 
    temp = ''
    if R in S : 
        ind = S.index(R)
        temp = temp + S[:ind]
        temp = temp + S[ind+len(R):]
        temp = temp + S[ind:ind+len(R)]
        return  temp
    else: 
        return -1 
S = raw_input()
R = raw_input()
S, R = T 
print(fun(S,R))