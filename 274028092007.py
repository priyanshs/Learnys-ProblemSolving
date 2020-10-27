'''
274028092007
Title: Anagrams 
Category: Strings - 3
Difficulty: Easy (TCS NQT)
Statement: 
You are given two strings S and R. Find out if the pair of strings are anagrams to each other. If the strings are palindrome print True on standard input else return False on standard input. 

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
'''

def check(s1, s2): 	
    a = sorted(s1) 
    b = sorted(s2)
	if ( a == b ): 
		return True 
	else: 
		return False
		
s1 = raw_input().split()
s2 = raw_input().split()
print(check(s1, s2)) 
