import sys

def alig() :
    N = int(input())
    li = []
    for i in range(N) :
        li.append(list(map(int,input().split())))
    li2 = sorted(li, key = lambda x : (x[0], x[1]))
    

    for i in li2 :    
        print(str(i[0]) + ' ' + str(i[1]))
    
    
if __name__ == "__main__" :
    alig()