'''
274028092007
Title: Anagrams 
Category: Strings - 3
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R. Find out if the pair of strings are anagrams to each other. If the strings are palindrome print True on standard input else return False on standard input. 

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
'''
S,R = raw_input().split()
set1 = set()
set2 = set()
for each in set(S): 
    set1.add((each, S.count(each)))
for each in set(R): 
    set2.add((each, R.count(each)))
if set1 == set2 : 
    print(True)
else: 
    print(False)