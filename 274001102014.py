
def left (S, M): 
    return S[-M+1:] + S[:M]

def right (S, M): 
    L = len(S)
    return S[L-M:] + S[:L-M]

S  = [int(i) for i in raw_input().split()]
R  = [int(i) for i in raw_input().split()]
T  = int(raw_input())
mov = [int(i) for i in raw_input().split()]

for each in mov : 
    if each > 0: 
        S = right(S,each)
    elif each < 0: 
        S = left(S,each)
    else: 
        pass
if S == R : 
    print("Password Accepted")
else:
    print("Try Again")