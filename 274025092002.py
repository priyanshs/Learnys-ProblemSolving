'''

274025092002
Title: Match Strings
Category: Strings - 2 
Difficulty: Easy (TCS NQT)
Statement: 
Two strings are provided to you as input, write a function to compare these strings together. Print characters that are common to both strings and occur the same number of times. 

Note: The strings are case sensitive.


'''

def compare(str1, str2): 
  foo = list()
  
  bar = set(str1).intersection(set(str2))
  
  for each in bar: 
      if str1.count(each) == str2.count(each): 
          foo.append(each)
  return foo

str1 = raw_input()
str2 = raw_input()

lis = (compare(str1, str2))
print(' '.join(lis))
