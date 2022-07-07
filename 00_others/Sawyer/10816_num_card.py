import sys
input = sys.stdin.readline




N = int(input())

N_dict = {}

N_list = sorted(list(map(int,input().split())))

for i in N_list :
    if i in N_dict:
        N_dict[i] += 1
    else :
        N_dict[i] = 1

M = int(input())
M_list = list(map(int,input().split()))


result = ''
for i in M_list:
    if i in N_dict :
        result += str(N_dict[i]) + ' '
    else :
        result += '0 '
print(result)
