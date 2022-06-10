import sys
input = sys.stdin.readline

def gita(n, price):
    result = []
    temp = 1001
    temp2 = 1001
    for i in price :
        temp = min(temp,i[0])
        temp2 = min(temp2,i[1])
    
    if n < 6 :
        result.append(temp)
        result.append(temp2*n)
        
 
    result.append(n//6*temp+n%6*temp2)
    result.append(n*temp2)
    result.append((n//6+1)*temp)
            

    print(min(result))




if __name__ == "__main__" :
    n,m = map(int,input().split())
    price = [list(map(int,input().split())) for _ in range(m)]

    gita(n,price)