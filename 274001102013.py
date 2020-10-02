'''
274001102013
Title: 
Category: Arrays 
Difficulty: Easy (TCS NQT)
Statement: 
Given a sorted array A of N elements, remove elements of the array whose index is either divisible by 3 or the value is divisible by 5. Print the newly created array on the standard output. 
'''
nums = list(map(int, raw_input().split()))
lis = list()
i = 0 
while i < len(nums)-1 :
    if not (i % 3 == 0 or nums[i] % 5 == 0): 
        lis.append(nums[i])
    i = i + 1
print(lis)