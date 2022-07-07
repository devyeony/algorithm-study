import sys

input = sys.stdin.readline

n = int(input())

grape = [int(input()) for _ in range(n)]

grape = [0] + grape

dp = [0 for _ in range(n+1)]

dp[1] = grape[1]

if n >= 2:
    dp[2] = grape[1] + grape[2]
if n >= 3: 
    dp[3] = max(dp[2], grape[1]+grape[3], grape[2]+grape[3])

if n >= 4:
    for i in range(4,n+1):
        dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3] +grape[i]+grape[i-1])

print(dp[n])

