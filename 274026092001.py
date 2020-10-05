'''
274026092001
Title: What’s in the string?
Category: Strings - 3 
Difficulty: Easy (TCS NQT)
Statement: 
Two strings are provided to you as input, write a function to compare these strings together. The comparison should be made between the ASCII sum of the characters stored in the string. 
Note: The strings are case sensitive, and thus considerations should be made. 
'''

def compare(str1, str2): 
  foo = sum([ord(i) for i in str1])
  bar = sum([ord(i) for i in str2])
  print(foo, bar)
  if foo == bar : 
    return True
  else: 
    return False

str1 = input()

str2 = input()

print(compare(str1, str2))
