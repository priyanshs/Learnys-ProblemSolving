'''
274001102008
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R. Count the minimum number of characters that need to be added to make the strings anagrams of each other. 
'''
S, R = input().split()
freq1 = {i : S.count(i) for i in S}
freq2 = {i : R.count(i) for i in R}
print(freq2, freq1)
if len(set(S)) >= len(set(R)): 
    diff1 = {i: freq1[i]- freq2[i] for i in set(freq1).union(set(freq2))}
else: 
    diff1 = {i: freq1[i]- freq2[i] for i in set(freq2).union(set(freq1))}
y = sum([abs(x) for x in diff1.values()])
print(y)