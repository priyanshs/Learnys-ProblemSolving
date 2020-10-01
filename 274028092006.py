'''
274028092006
Title: Palindrome and Reverse 
Category: Strings - 1 
Difficulty: Medium (TCS NQT)
Statement: 
Given a string S, split the string in two equal parts. Reverse the string each part and check if they form a palindrome. If the resultant string is palindrome, return True else return False.
'''
def palin(S):
    l = len(S) 
    R = S[:l//2]
    Q = S[l//2:]
    print(R,Q)
    if ((Q+R)[::-1] == Q+R): 
        return True 
    else: 
        return False

print(palin(input()))