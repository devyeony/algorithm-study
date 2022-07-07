def mi_val(value) :
    result = 0 
    for i in trees:
        if i > value :
            result += i-value
    
    return result


def cut_tree() :

    N,M = map(int,input().split())
    
    global trees
    
    trees = sorted(list(map(int,input().split())))
    
    start = 0
    
    end = max(trees)
    
    while start <= end : 
        
        mid = (start + end) // 2 
        value = mi_val(mid)
        if value >= M :
            start = mid + 1
        else : 
            end = mid -1
    print(end)
       
    
   
    

if __name__=="__main__" :
    cut_tree()