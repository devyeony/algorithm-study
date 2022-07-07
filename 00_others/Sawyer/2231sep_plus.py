def sep_plus() :
    N = int(input())
    if N > 17 :
        M = N - len(str(N)) * 9
    else :
        M = 0
        
    
    for i in range(M,N+1) :
        
        result = solution(i) + i

        if result == N :
            print (i)
            break
        elif i == N:
            print('0')
            break
        
def solution(n):
    N=[int(i) for i in str(n)]

    return sum(N)


if __name__=="__main__" :
    sep_plus()