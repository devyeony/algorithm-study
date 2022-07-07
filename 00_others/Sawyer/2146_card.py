from collections import deque 

def card2_2146():
    N = int(input())
    card = [ i for i in range(1,N+1)]
    
    card2 = deque(card)
    while True :
        if len(card2) == 1 :
            print(card2[0])
            break
        
        else :
            card2.popleft()
            if len(card2) == 1 :
                print(card2[0])
                break
            card2.append(card2[0])
            card2.popleft()

if __name__=="__main__" :
    card2_2146()