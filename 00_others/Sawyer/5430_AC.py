from collections import deque

def AC() :
    T = int(input())
    for i in range(T):
        p = str(input())
        n = int(input())
        
        list_str = str(input())
        
        if list_str == '[]':
            n_list = []
        else : 
            n_list = deque(list(map(int,list_str[1:-1].split(','))))
        
        ### 입력받기 끝
      
        pop_lr = 'L'
        
        
        for j in p:
            if j == 'R' :
                if pop_lr == 'L' :
                    pop_lr = 'R'
                else :
                    pop_lr = 'L'
            else :
                if len(n_list) != 0 :
                    if pop_lr == 'L' :
                        n_list.popleft()
                    else :
                        n_list.pop()
                else :
                    print('error')
                    break
        else :
            if len(n_list) == 0 :
                print([])            
            elif p.count('R') % 2 == 1 :
                n_list.reverse()
                print(str(list(n_list)).replace(' ',''))
            else :
                print(str(list(n_list)).replace(' ',''))
    
    
if __name__ == "__main__" :
    AC()