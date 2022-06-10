import sys
import math

input = sys.stdin.readline
num_str = str(math.factorial(int(input())))

temp = 0
for i in num_str[::-1] :
    if i == '0':
        temp += 1
        
    else :
        break
        
print(temp)