import sys


input = sys.stdin.readline

N,S,M = map(int,input().split()) # 곡의 개수, 시작 , 최대값

music_list = list(map(int,input().split()))

DP = [[False]*(M+1) for _ in range(N+1)]

DP[0][S] = 1


for i in range(1,N+1) :
    for j in range(M+1):
        if DP[i-1][j]!=0:
            if 0<=j+music_list[i-1]<=M :
                DP[i][j+music_list[i-1]]=1
            if 0<=j-music_list[i-1]<=M:
                DP[i][j-music_list[i-1]]=1
ans =-1
#볼륨의 최대값을 출력하기 위해 내림차순으로 반복문 실행 
for i in range(M, -1, -1):
    if DP[N][i] : #최대값 발견하면 중단 
        ans = i
        break
    
print(ans)           
            
        
        


