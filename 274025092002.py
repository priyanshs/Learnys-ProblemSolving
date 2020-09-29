# Two strings are provided to you as input, write a function to compare these strings together. 
# Print characters that are common to both strings and occur the same number of times. 

def compare(str1, str2): 
  foo = list()
  
  bar = set(str1).intersection(set(str2))
  
  for each in bar: 
      if str1.count(each) == str2.count(each): 
          foo.append(each)
  return foo

str1 = input('E1:')

str2 = input('E2:')

print(compare(str1, str2))
