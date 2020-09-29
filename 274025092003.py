#Two strings are provided to you as input, write a function to compare these strings together. 
#The comparison should be made between the ASCII sum of the characters stored in the string. 
#Note: The strings are case sensitive, and thus considerations should be made. 

def compare(str1, str2): 
  foo = sum([ord(i) for i in str1])
  bar = sum([ord(i) for i in str2])
  if foo == bar : 
    return True
  else: 
    return False

str1 = input('E1:')

str2 = input('E2:')

print(compare(str1, str2))
