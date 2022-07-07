def bee() :
    N = int(input())
    result = 1
    plus = 0
    value = 1
    while True :
        if N <= value :
            print(result)
            break
        else:
            plus += 6
            value += plus
            result +=1
        
    
    

if __name__=="__main__" :
    bee()
    
    
    
    # 1 7 19 37 61  
    #  6 12 18 24 
    #   6  6  6