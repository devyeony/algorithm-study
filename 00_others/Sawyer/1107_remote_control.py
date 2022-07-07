# 가장 가까운수

def remote() :
    
    N = str(input())
    number = int(input())
    button = [i for i in range(10)]
    if number != 0 :
        abc = list(map(int,input().split()))
        for i in abc:
            button.remove(i)
    # button은 안고장난 버튼
    button = set(button)

    

    result = abs(100 - int(N))
    
    
    
    for i in range(1000001) :
        for j in str(i) :
            if int(j) not in button:
                break
        else :
            result = min(result, len(str(i)) + abs(i - int(N)))
                
    print(result)
    
    
if __name__ == "__main__" :
    remote()