'''
274001102002
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
Given a simple string S of length more than 5 and words A and B as input. Split the string S at every occurrence of the A or B. 
Note. Set(A) intersection with Set(B) = Null 
'''

S, A, B = input().split()
S = S.split(A)
print(S)
temp = S
for val in S : 
    if B in val: 
        temp.extend(val.split(B))
        temp.remove(val)
for each in temp : 
    if '' == each : 
        temp.remove('') 
print(temp)