import sys

n = int(sys.stdin.readline())


n_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

result = sorted(n_list, key = lambda x : (x[1],x[0]))


for i in result:
    print(str(i[0]) + ' ' + str(i[1]))