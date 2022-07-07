def rat() :
    while 1 :
        line = str(input())
        if '0 0 0' ==  line:
            break
        else :
            temp = list(map(int, line.split()))
            temp.sort()
            if temp[0]**2 + temp[1] **2 == temp[2] ** 2 :
                print('right')
            else :
                print('wrong')
if __name__ == "__main__" :
    rat()