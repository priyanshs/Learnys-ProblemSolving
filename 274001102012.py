'''
274001102012
Title: 
Category: Arrays 
Difficulty: Easy (TCS NQT)
Statement: 
Given a sorted array A of N elements, remove elements from the start of the array till the sum of the array becomes half of what it was previously. 
'''
nums = [int(i) for i in raw_input().split()]
su = sum(nums)
while sum(nums) > su//2 : 
    nums.pop(0)
print(nums)