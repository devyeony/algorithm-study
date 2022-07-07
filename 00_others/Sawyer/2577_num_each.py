class NUM :
    def __init__(self,n,m,k) :
        self.n = n
        self.m = m
        self.k = k
    
    def numbers(self) :
        result = self.n * self.m * self.k
        
        for i in range(10) :
            print(str(result).count(str(i)))
        

    
    
if __name__ == "__main__" :
    n = int(input())
    m = int(input())
    k = int(input())
    t = NUM(n,m,k)
    t.numbers()