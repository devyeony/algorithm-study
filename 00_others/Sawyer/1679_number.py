import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
k = int(input())
memo = [False for _ in range((n_list[-1]*k) + 1)]

for num in n_list:
    memo[num] = True

dp = [set() for _ in range(k+1)]
dp[1] = set(n_list)

for i in range(2, len(dp)):
    before = dp[i-1]
    for b in before:
        for num in n_list:
            memo[b+num] = True
            dp[i].add(b+num)

for num in range(1, len(memo)):
    if not memo[num]: break

who = 'holsoon' if num % 2 == 0 else 'jjaksoon'
print('{} win at {}'.format(who, num))
