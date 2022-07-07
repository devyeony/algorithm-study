import sys

input = sys.stdin.readline

def _2920() :
    num_list = list(map(int,input().split()))
    
    asc = [i for i in range(1,9)]
    desc = [i for i in range(8,0,-1)]
    
    if num_list == asc :
        print('ascending')
    elif num_list == desc :
        print('descending')
        
    else :
        print('mixed')


if __name__ == "__main__" :
    _2920()