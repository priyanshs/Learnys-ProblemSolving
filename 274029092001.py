'''
274029092001 (C) 
Title: Suffix that
Category: Strings - 2
Difficulty: Medium (TCS NQT)
Statement: 
You are given a long string separated by spaces. The task at your hand is to find the longest suffix between the string value. A suffix needs to be continuous. If there is no such string available print an empty string on the standard output.
'''
S = input().split()
S = sorted(S, key = len)
t = S[0]
ma = 10**10
for i in range(1,len(S)): 
    temp = 0 
    for j in range(-1, -len(S[i]) - 1 ,-1): 
        if j >= -len(S) and S[i][j] == t[j] : 
            temp = temp + 1
    ma = min(temp, ma)

print(t[-ma: ])
