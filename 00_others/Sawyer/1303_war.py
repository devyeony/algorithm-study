import sys
from collections import deque


def bfs(graph, start):
    num = [0] * (n+1) # 그래프와의 거리를 넣을 리스트
    visited = [start] # 방문여부
    queue = deque()  # popleft를 위해서 deque사용
    queue.append(start) # 큐에 출발위치 넣어주기

    while queue: # 큐에 값이 있으면 계속돌아주기
        a = queue.popleft() # 큐에 먼저들어온값 빼주기
        for i in graph[a]: # 그래프리스트의 [a]가 value이기때문에 확인
            if i not in visited: # 방문안한 곳이면 방문 
                num[i] = num[a] + 1 # 종목이 기존 경로에 있으면 기존거리 + 1
                visited.append(i) # 방문리스트에 추가
                queue.append(i) # 큐에 넣어주기
    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    # graph = [[] for _ in range(n+1)] 
    # for i in range(m):
    #     a, b = map(int, sys.stdin.readline().split())
    #     graph[a].append(b)
    #     graph[b].append(a)

    # result = []
    # for i in range(1, n+1):
    #     result.append(bfs(graph, i))
    temp = [] 
    graph = [temp + [] input()]
    print(result.index(min(result))+1)