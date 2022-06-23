# import sys
# from collections import deque
# input = sys.stdin.readline

# pol = str(input().strip())

# idx_list = []
# for i in range(len(pol)) :
#     if pol[i] == '.' :
#         idx_list.append(i)

# pol_list = pol.split('.')

# que = deque(pol.split())

# is_false = False
# while True
#     if len(i) == 0 :
#         result += '..'
#         continue
#     while True :
#         if len(i) == 0 :
#             break
#         elif len(i) >= 4 :
#             result += 'AAAA'
#             i = i[4:]
#         elif len(i) == 2 :
#             result += 'BB'
#             i = i[2:]
#         else :
#             is_false = True
#             break
            
# if is_false :
#     print(-1)
# else :
#     print(result)



board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)