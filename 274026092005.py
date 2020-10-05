'''
274026092005
Title: Permutations 
Category: Strings - 1
Difficulty: Medium (TCS NQT)
Statement: 
You are given an alphanumeric string of length greater than 5. Print all possible strings that can be created by permuting the last three characters. 
'''

string = input()
l = len(string)
list1 = list()
if l >=3: 
    list1.append(string)
    list1.append(string[:l-2] + string[l-1] + string[l-2])
    list1.append(string[:l-3] + string[l-1] + string[l-2] + string[l-3])
    list1.append(string[:l-3] + string[l-1] + string[l-3] + string[l-2])
    list1.append(string[:l-3] + string[l-2] + string[l-1] + string[l-3])
    list1.append(string[:l-3] + string[l-2] + string[l-3] + string[l-1])
    list1 = (list(set(list1)))
    list1 = [i for i in list1 if len(i) == l]
    print(list1)
else: 
    print("Invalid Input")