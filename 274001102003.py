'''
274001102003
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
Given a string S and a numeric M, rotate the string left and right by M and check if the resultant string forms a palindrome. 
'''

S, M = input().split()
M = int(M)
L = len(S)
left  = S[M:] + S[:M]
right = S[L-M:] + S[:L-M]
print(left, right)
if left == left[::-1] or right == right[::-1]: 
    print(True)
else: 
    print(False)
