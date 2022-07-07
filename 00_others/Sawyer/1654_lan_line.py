import sys

def line() :
    K,N = map(int,input().split())
    
    line = [int(sys.stdin.readline()) for i in range(K)]
    start, end = 1, max(line)
   
    while start <= end :
        mid = (start + end) // 2
        count = 0 
        for i in line:
            count += i//mid
        if N <= count  :
            start = mid + 1
        else :
            end = mid - 1
    
    print(end)
if __name__ == "__main__" :
    line()