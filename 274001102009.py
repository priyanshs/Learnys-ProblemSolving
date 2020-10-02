'''
274001102009
Title: 
Category: Arrays 
Difficulty: Easy (TCS NQT)
Statement: 
You are given N bags of chocolates which need to be distributed between two classes A and B. Each of these bags contain a random amount of chocolates which shall be given to you as input. The task at hand is to divide the bags so that each class gets a similar number of chocolates. Additionally, you have to select the bags contiguously.  
'''
N = int(input())
choc = [int(i) for i in input().split()]
su = sum(choc) 
i = 0 
temp = 0 
while temp < su // 2: 
    temp += choc[i]
    i += 1 
print(choc[:i], choc[i:])