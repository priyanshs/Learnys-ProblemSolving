'''
274028092003 (C) 
Title: Repeat and count 
Category: Strings - 3
Difficulty: Medium (TCS NQT)
Statement: 
You are given four inputs, two strings, S and R along with integers M and N. The task at hand is to repeat the string according to its corresponding integer. Take for instance, string S should be repeated M times. Write an algorithm to calculate the difference between the resultant strings. Each character has an associated integer ASCII value which should be used while finding the difference. 
'''
S,R,M,N = input().split()
if int(M) < 0 or int(N) < 0 : 
    AcS = sum([ord(i) for i in S]) * int(M)
    AcR = sum([ord(i) for i in R]) * int(N)
    print(AcS - AcR)
else: 
    print(0)