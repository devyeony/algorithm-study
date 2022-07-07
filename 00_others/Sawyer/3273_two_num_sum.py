import sys
input = sys.stdin.readline
def solution(n,n_list,x):
    n_list.sort()
    result = 0
    left, right = 0, n-1
    
    while left < right :
        tmp = n_list[left] + n_list[right]
        if tmp == x:
            result +=1
        if tmp < x :
            left +=1
            continue
        right-=1
    print(result)


if __name__ == '__main__':
    n = int(input())
    n_list = list(map(int,input().split()))
    x = int(input())
    solution(n,n_list,x)