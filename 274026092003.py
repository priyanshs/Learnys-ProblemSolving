'''
274026092003
Title: Reduce to Frequency 
Category: Strings - 1
Difficulty: Medium (TCS NQT)
Statement: 
You are given a string as input. Arrange the string in alphabetical order and print the frequency next to each character. 

Note: The strings are case sensitive, and thus considerations should be made. 

'''
st = raw_input()
li = list(st)
li.sort()
a = ""
for i in sorted(set(li)):
    a = a + i + str(li.count(i))
print(a)
