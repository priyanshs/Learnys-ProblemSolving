'''
274028092006
Title: Palindrome and Reverse 
Category: Strings - 1 
Difficulty: Medium (TCS NQT)
Statement: 
Given a string S, split the string in two from the center. Reverse the string each part and check if they form a palindrome. If the resultant string is palindrome, return True else return False.

Note: If the sting is of odd length the character should be added to the right string.
'''
def palin(S):
    l = len(S) 
    R = S[:l//2]
    Q = S[l//2:]
    if ((Q+R)[::-1] == Q+R): 
        return True 
    else: 
        return False

print(palin(raw_input()))