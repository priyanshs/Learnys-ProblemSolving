'''

274025092001 (C) 
Title: Are all strings equal? 
Category: Strings - 2 
Difficulty: Difficult (TCS NQT)
Statement: 
Two strings are provided to you as input, write a function to compare these strings together. Two strings are considered equal if they contain the same number of alphabets each and match the character count of each individual character present. 

Note: The strings are not case sensitive, and thus conversions should be made. 

'''
def compare(str1, str2): 
  str1 = str1.lower()
  str2 = str2.lower()
  foo = dict()
  bar = dict()
  if (str1 == '' or str2 == ''): 
    return False

  if len(str1) == len(str2): 
    for each in set(str1):
      foo[each] = str1.count(each)
    for each in set(str2):
      bar[each] = str2.count(each)

    if foo.keys() == bar.keys(): 
      flag = 1 
      for each in foo.keys(): 
        if foo[each] == bar[each]: 
          flag = 0
        else: 
          return False
        if flag == 0: 
          return True 
    else: 
      return False
  else: 
    return False


str1 = raw_input()
str2 = raw_input()

print(compare(str1,str2))