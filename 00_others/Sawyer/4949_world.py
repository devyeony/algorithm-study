import sys

def balance() :

    input = sys.stdin.readline

    while 1:
        string = input().rstrip()
        stack = []
        true_flag = 1


        for cha in string:
            if cha == '(' or cha == '[':
                stack.append(cha)
            elif cha == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    true_flag = 0
                    break
            elif cha == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    true_flag = 0
                    break

        if string == '.':
            break

        print("yes" if true_flag and not stack else "no")


if __name__ == "__main__" :
    balance()