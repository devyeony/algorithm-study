def alig():
    N = int(input())
    abc = []

    for i in range(N):
        a = list(input().split()) 
        abc.append( [int(a[0]), i, a[1]] )
    
    d = sorted(abc, key = lambda x : x[0] )
    
    for i in range(N) :
        print(str(d[i][0]) + ' ' + str(d[i][2]))
        
if __name__ == "__main__" :
    alig()