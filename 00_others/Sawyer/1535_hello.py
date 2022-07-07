N = int(input()) 
L = [int(x) for x in input().split()] # 인사하면 잃는 체력
J = [int(x) for x in input().split()] # 인사하면 얻는 기쁨
L, J = [0] + L, [0] + J  
dp = [[0 for _ in range(101)] for _ in range(N+1)] # dp[잃은 체력 순서][현재체력] = 얻은 기쁨
for i in range(1, N+1): 
    for j in range(1, 101): 
        if L[i] <= j: #남은 체력이 현재 체력보다 많거나 같으면  
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i]) # dp[i-1][j]는 이전 스텝 중에 최대값을 찾아야되기 때문에 넣었고 dp[i-1][j-L[i]] + J[i]는 이전무게 
        else: 
            dp[i][j] = dp[i-1][j] 

print(dp[N][99])

