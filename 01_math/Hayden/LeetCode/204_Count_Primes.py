# #2 - LeetCode : 204. Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        prime_list = [True] * (n+1)
        prime_list[0] = False
        if n >= 1:
            prime_list[1] = False
        for i in range(2, n//2+1):
            if prime_list[i]:
                for j in range(i*2, n+1, i):
                    prime_list[j] = False
        prime_list.pop()
        return prime_list.count(True)


sol = Solution()
print(sol.countPrimes(10))
print(sol.countPrimes(0))
print(sol.countPrimes(1))
