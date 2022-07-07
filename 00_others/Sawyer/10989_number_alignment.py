import sys


def alig() :
    N = int(input())
    li1 = [0] * 10001
    
    for _ in range(N) :
        li1 [int(sys.stdin.readline())] +=1
    


    for j in range(len(li1)):
        if li1[j] != 0 :
            for _ in range(li1[j]) :
                print(j)
            
    
if __name__ == "__main__" :
    alig()