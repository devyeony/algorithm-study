N = int(input())

def logic(word : str) -> int:
    temp = 0
    result = 0
    for i in word:
        if i == 'O':
            temp+=1
            result+=temp
        else :
            temp = 0
    
    return result
        

for _ in range(N):
    print(logic(str(input())))


