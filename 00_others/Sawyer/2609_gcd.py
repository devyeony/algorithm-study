from math import gcd

def lcm(x,y) :
    return x * y // gcd(x,y)



def dddd():
    M,N = map(int, input().split())
    print(gcd(M,N))
    print(lcm(M,N))


    
if __name__=="__main__" :
    dddd()
    