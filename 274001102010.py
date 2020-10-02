'''
274001102010
Title: 
Category: Arrays 
Difficulty: Easy (TCS NQT)
Statement: 
Given an array of numbers S, you are tasked to convert the numbers given into a two dimensional representation by splitting the array into N rows with M columns (Row Major). Print the newly created representation. 
'''
nums = [int(i) for i in raw_input().split()]
N, M = [int(i) for i in raw_input().split()]
arr  = list()
for i in xrange(N): 
    arr.append(nums[i*M:i*M + M])
print(arr)