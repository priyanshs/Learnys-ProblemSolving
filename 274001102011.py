'''
274001102011
Title: 
Category: Arrays 
Difficulty: Easy (TCS NQT)
Statement: 
N students are playing musical chairs. There are only N-2 chairs available for students to sit. With each movement the students are rotating in an anti-clockwise direction (left shift). You are given the number of shifts students make as S. Students at the far ends are removed from the game. Find out these students. 
'''
S = [int(i) for i in raw_input().split()]
M = int(raw_input())
S  = S[-M+1:] + S[:M]
print(S[0], S[-1])