import sys
input = sys.stdin.readline().rstrip


def dp(n : int) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    else :
        return dp(n-1) + dp(n-2)



N = int(input())


result = dp(N) 



print(type(result))
print(result%10007)