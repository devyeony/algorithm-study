def sugar() :
    
    N = int(input())

    if N == 4 or N ==7 :
        print(-1)
            
    else :
        
        M = N // 5 
        m = N % 5
        
        if m == 0 :
            print(M)
        elif m == 1 :
            print(M + 1)
        elif m == 2 :
            print(M + 2)
        elif m == 3 :
            print(M + 1)
        elif m == 4 :
            print(M + 2)
        
            
    
    


    
if __name__ == "__main__" :
    sugar()