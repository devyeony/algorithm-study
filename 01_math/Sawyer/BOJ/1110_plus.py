import sys
from collections import deque

input = sys.stdin.readline

def solution(n):
    result = 0
    first = n 
    while True:
        result +=1
        if len(str(n)) > 1 :
            sum = int(str(n)[0]) + int(str(n)[1])
            if len(str(sum)) > 1:
                n = int(str(n)[1] + str(sum)[1])
            else :
                n = int(str(n)[1] + str(sum)[0])
        else :
            n = int(str(n) + str(n))

        if first == n :
            break

        
    return result



    

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
   