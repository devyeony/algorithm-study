import math

def is_prime_number(x):
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
        if x % i == 0:# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True # 전부 나눠떨어지지 않는다면 소수임



def do() :
    m = int(input())
    n_list = list(map(int,input().split()))
    result = 0
    for i in n_list :
        if i == 1 :
            pass
        
        elif is_prime_number(i) :
            result += 1

    print(result)
    


if __name__ == "__main__" :
    do()