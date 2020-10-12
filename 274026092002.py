'''
274026092002 (C)
Compress Recurrences 
Strings - 1
Difficult (TCS NQT)
You shall be given a string as an input and a minimum compression value as inputs. The task at hand is to compress the string. If a character is repeated more than the minimum compression value, the character is compressed. If a compression is made, attach the numeric value. 

Note: The strings are case sensitive, and thus considerations should be made. 
'''
def compare(str1, int1):
    str2 = ""
    i = 0 
    while i < len(str1): 
        j = i
        count = 0 
        while j < len(str1):
            if str1[i] == str1[j]:
                count += 1  
                j = j + 1
            else: 
                break
        if count > int1 - 1:
            str2 = str2 + (str1[i] + str(count))
            i = i + count
        else: 
            str2 += str1[i]
            i = i + 1
    return str2




str1 = 'tYYbFbjCIIWtttIHHHcRt'*2 #input('E1:')
print(str1)
int1 = 2 #int(input('E2:'))

print(compare(str1, int1))
