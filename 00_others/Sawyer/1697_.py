import sys
from collections import deque
input = sys.stdin.readline





def bfs(n, m, dist):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m :
            print(x_loca[x])
            break

        for j in (x-1,x+1,x*2):
            if 0 <= j <= MAX and not x_loca[j] :
                x_loca[j] = x_loca[x] + 1
                q.append(j)



if __name__ == '__main__':
    n, m = map(int, input().split())
    MAX = 100000
    x_loca = [0] * (MAX+1)
    bfs(n,m,x_loca)