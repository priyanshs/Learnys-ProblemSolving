def compare(str1, str2): 
  str1 = str1.lower()
  str2 = str2.lower()
  foo = dict()
  bar = dict()

  if len(str1) == len(str2): 

    for each in set(str1):
      foo[each] = str1.count(each)
    for each in set(str1):
      bar[each] = str1.count(each)
    
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


str1 = input()
str2 = input()

print(compare(str1,str2))