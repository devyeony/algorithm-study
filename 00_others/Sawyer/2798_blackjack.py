from itertools import combinations

def find_nearest(a, M):
    lst = [item for item in a if item <= M]
    return max(lst)


def black() :
    N, M = map(int,input().split())
    card_ = list(map(int,input().split()))
    result = []
     
    temp = list(combinations(card_,3))
    
    
    for i in temp:
        result.append(sum(i))
   
    result.sort()
    print(find_nearest(result, M))


if __name__ == "__main__" :
    black()