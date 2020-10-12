'''
274001102005
Title: 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R as inputs. Remove all the instances of R from S. To keep the character of string S the same add the neighbours of the removed instance to the end. For example, you are S = Hello R = ll the resultant string would be Heoeo. The length of R will always be even. 
'''
S, R = input().split()
st = ""
Q = S.split(R)
for i in range(1, len(Q)):
    print(Q[i-1]) 
    if len(Q[i-1]) > 0: 
        st = st + Q[i-1] + Q[i-1][-1] * (len(R))
st = st + Q[-1] 
print(st)
