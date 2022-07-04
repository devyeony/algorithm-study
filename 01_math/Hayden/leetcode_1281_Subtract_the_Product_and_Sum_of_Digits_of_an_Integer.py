# #2 - LeetCode : 1281. Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(i) for i in str(n)]
        product = 1
        sum = 0
        for i in nums:
            product *= i
            sum += i
        return product - sum


sol = Solution()
print(sol.subtractProductAndSum(234))
print(sol.subtractProductAndSum(4421))
