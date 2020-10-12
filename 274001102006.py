'''
274001102006
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R as well as a number N as inputs. At indices, starting at 0, within S which are divisible by N, insert the string R. 
'''
S = input()
R = input()
N = int(input())

st = ""
for i in range(len(S)): 
    if i % N == 0: 
        st += R
    st += S[i]
print(st)