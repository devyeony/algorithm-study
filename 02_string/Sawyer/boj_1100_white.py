import sys

input = sys.stdin.readline


chess = []
color = ['white','black']
them = 1
white_pla = []
result = 0
for _ in range(8) :
    word = str(input())
    if them == 0 : 
        them =1
    else :
        them = 0 
    for i in range(8):
        if i % 2 == them :
            if word[i] == 'F' :
                result +=1
print(result)