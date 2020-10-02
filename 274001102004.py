'''
274001102004
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
As part of developing a new password management system, you are given the task to validate if the password provided is correct or not. Each password phrase S and R will be followed by T numeric values. These values can be positive representing right rotation by given value or negative which is left rotation with the given value. Perform the operations on S and compare the resultant with R if they are the same print “password accepted” else print “try again”.  
'''
def left (S, M): 
    return S[-M+1:] + S[:M]
def right (S, M): 
    L = len(S)
    return S[L-M:] + S[:L-M]

S,R = input().split()
T = int(input())
mov = [int(i) for i in input().split()]
for each in mov : 
    if each > 0: 
        S = right(S,each)
    elif each < 0: 
        S = left(S,each)
    else: 
        pass
if S == R : 
    print("Password Accepted")
else:
    print("Try Again")