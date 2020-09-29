
# You shall be given a string as an input and a minimum compression value. 
# The task at hand is to compress the string. 
# If a character is repeated more than the minimum compression value, the character is compressed. 
# If a compression is made, attach the numeric value. 
#Note: The strings are case sensitive, and thus considerations should be made. 

Sample Case: 
>>> aaabb 2 
>>> a3b2










Q : without constraint but consecutive 
Q : character frequency (arranged alphabetically)

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




str1 = 'aaabb' #input('E1:')
print(str1)
int1 = 3 #int(input('E2:'))

print(compare(str1, int1))
