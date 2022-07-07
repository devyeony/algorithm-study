import sys
input = sys.stdin.readline


def solution(n,s,n_list):
    result = 0
    the_sum = n_list[0]
    left, right = 0, 0
    answer = 100001
    while True :
        if the_sum >= s :
            the_sum -= n_list[left]
            answer = min(answer, right - left + 1)
            left += 1
        else :
            right += 1
            if right == n :
                break
            the_sum += n_list[right]
    return answer

if __name__ == '__main__':
    n , s = map(int,input().split())
    n_list = list(map(int,input().split()))
    answer = solution(n,s,n_list)

    print (0) if answer == 100001 else print(answer)