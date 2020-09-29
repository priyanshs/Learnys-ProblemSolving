'''
274026092004
Title: Consecutive Frequency 
Category: Strings - 1
Difficulty: Easy (TCS NQT)
Statement: 
You are given a string as input. The string contains only lowercase characters. Find the frequency of characters which are repeated consecutively. Print these strings in the format specified.
'''

string = input()
output = ""
i = 0
while i < len(string):
    count = 0 
    for j in range(i+1,len(string)): 
        if string[i] != string[j]: 
            break
        else: 
            count += 1 
    if count > 0: 
        output += string[i] + str(count+1)
    i = i + count + 1
print(output)