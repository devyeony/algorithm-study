import sys

input = sys.stdin.readline


T = int(input())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))


for _ in range(T):
    n_list = list(map(int,input().split()))
    n_list.sort(reverse=True)
    print(lcm(n_list[0],n_list[1]))
