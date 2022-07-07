def zero() :
    N = int(input())
    n_list = []
    result = []
    for i in range(N) :
        n_list.append(int(input()))
        if n_list[-1] != 0 :
            result.append(n_list[-1]) 
        else : 
            result.pop()
            
            
    print(sum(result))

if __name__ == "__main__" :
    zero()