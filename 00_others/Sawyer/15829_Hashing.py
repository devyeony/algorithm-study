import sys

def ordd (alpa : str) :
    return ord(alpa) - 96


N = int(input())


alphabet = str(input())

result = 0
temp = 0

for i in alphabet :
    result += ordd(i) * (31**temp)
    temp +=1

print(result%1234567891)