import time   
from sys import stdin, stdout

start = time.time()  # 시작 시간 저장




def find() :
    N = stdin.readline()
    li1 = set(stdin.readline().split())
    M = stdin.readline()
    li2 = stdin.readline().split()

    
    
    
    for l in li2:
        stdout.write('1\n') if l in li1 else stdout.write('0\n')

#     result = []
#     for i in li2 :
#         if i in li1:
            
#             result.append('1')
#         else : 

#             result.append('0')
    
#     for j in result :
#         print(j)
        
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

if __name__=="__main__" :
    find()
    
    