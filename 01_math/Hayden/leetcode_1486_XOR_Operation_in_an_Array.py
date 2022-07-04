# #2 - 1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer: int = start
        for i in range(1, n):
            answer ^= (start + 2 * i)
        return answer


sol = Solution()
print(sol.xorOperation(5, 0))
print(sol.xorOperation(4, 3))

'''
비트 XOR(배타적 OR) 연산자
: XOR 연산은 입력값이 같지 않으면 1을 출력. 파이썬에서는 ^ 기호를 사용
: 참고) https://ko.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-bitwise-operation
'''