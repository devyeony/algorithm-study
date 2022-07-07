import sys
import time
import math

input = sys.stdin.readline
start = time.time()

input = sys.stdin.readline

N = int(input())

num = 0
idx = 1

n_list = [1]

m_list = [1]
t= 2
dp = [float('inf')] * (N + 1)

while True :
    if m_list[-1] >= N :
        break
    n_list.append(n_list[-1]+t)
    m_list.append(m_list[-1]+n_list[-1])
    t+=1
num = m_list[-1]
result = 0 
n = -1

print(m_list)

for i in range(1, N + 1):
    for num in m_list:
        if num == i:
            dp[i] = 1
            break
        if num > i: break
        dp[i] = min(dp[i], 1 + dp[i - num])
print(dp[N])
math.factorial(100000) 
end = time.time() 
print(f"{end - start:.5f} sec")


