import sys

input = sys.stdin.readline


n = str(input().strip())

result = 0
for i in n :
    result += int(i)**5

print(result)