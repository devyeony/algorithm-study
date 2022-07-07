import sys
from collections import defaultdict,deque
input = sys.stdin.readline
   
def que() :
    qu = deque()
    N = int(input())
    
    for _ in range(N):
        order = str(input())
        
        if order[0] == 'p' and order[1] == 'u' :
            push = order.split()
            qu.append(int(push[1]))
            continue
        else :
            order = order.split()[0]
            if order == 'pop' :
                try :
                    print(qu.popleft())

                except IndexError :
                    print('-1')

            elif order == 'size' :
                print(len(qu))

            elif order == 'empty' :
                if len(qu) == 0 :
                    print(1)
                else:
                    print(0)

            elif order == 'front' :
                
                try :
                    print(qu[0])

                except IndexError:
                    print(-1)


            elif order == 'back' :
                try :
                    print(qu[-1])

                except :
                    print(-1)
                
    
if __name__ == "__main__" :
    que()