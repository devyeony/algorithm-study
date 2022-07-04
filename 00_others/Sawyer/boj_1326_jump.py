from collections import deque
import sys
input = sys.stdin.readline



def dfs(a,b,bridge,N) :
    q = deque() # deque 생성
    q.append(a-1) # 리스트에서는 0부터시작하기때문에 -1
    check = [-1] * N # -1로 채워진 리스트 
    check[a-1] = 0 # 출발지점은 0 점프를안해도 도착하므로 0
    while q: # q값이 채워져있으면 계속 동작
        node = q.popleft() # FIFO 먼저들어온값을 node값에 넣는다
        for n in range(node, N, bridge[node]) : # node 값에서  N 까지(N은포함하지않는다.) bridge[node]는 점프값 만큼 차이를 두고 
            if check[n] == -1: # 방문안하곳이면 
                q.append(n)  # deque에 추가 해서 이값도 while문에들어간다.
                check[n] = check[node] +1 # check값은 폴짝(점프) 횟수
                if n == b-1 :         # 도착지점 도착
                    return check[n]  # 폴짝(점프) 한 횟수 return 
        for n in range(node, -1, -bridge[node]):# 도착지점이 뒤쪽인 경우
            if check[n] == -1 :
                q.append(n)
                check[n] = check[node] +1
                if n == b-1 :
                    return check[n]
    return -1


N = int(input()) # 징검다리 개수 입력받기
bridge = list(map(int,input().split())) #징검다리입력
a,b = map(int,input().split()) # a에서 b로 건너야함
print(dfs(a,b,bridge,N))