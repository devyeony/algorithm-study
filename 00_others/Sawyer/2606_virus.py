import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, graph):
    result = 0
    que = deque()
    




if __name__ == "__main__" :
    n = int(input())
    m = int(input())
    graph = [0] * (m+1)
    for _ in range(m) :
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(n,graph))

   