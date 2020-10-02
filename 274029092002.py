'''
274029092003
Title: The Last Word 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
Given a string s consisting of upper/lower-case alphabets and empty characters ' ', ‘*’, ‘#’, ‘&’, return the length of the last word (last word means the last appearing word if we loop from left to right) in the string. If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
'''
characters = '*', '#', '&',
string = input()
string = string.split()
temp = string 
for val in temp: 
    if '#' in val:
        temp.remove(val)
        temp.extend(val.split('#'))
    if '' in temp: 
        temp.remove('')
for val in temp:
    if '*' in val:
        temp.remove(val)
        temp.extend(val.split('*'))
    if '' in temp: 
        temp.remove('')
for val in temp:
    if '&' in val:
        temp.remove(val)
        temp.extend(val.split('&'))
    if '' in temp: 
        temp.remove('')        
print(temp)

'''
for each in characters: 
    for val in string: 
        if each in val : 
            val = val.split(each)
            print(val)
    if each in val : 
        string.extend(val)

print(string)

    '''