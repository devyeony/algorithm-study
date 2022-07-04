import sys
input = sys.stdin.readline
def solution(n,n_list):
    n_list.sort()
    result = 0
    left, right = 0, n-1
    answer = float('inf')
    final = []
    while left < right :
        tmp = n_list[left] + n_list[right]
        if abs(tmp) < answer :
            answer = abs(tmp)
            final = [n_list[left], n_list[right]]
        if tmp < 0 :
            left+=1 
        else:
            right -= 1
    print(final[0])
if __name__ == '__main__':
    n = int(input())
    n_list = list(map(int,input().split()))
    solution(n,n_list)