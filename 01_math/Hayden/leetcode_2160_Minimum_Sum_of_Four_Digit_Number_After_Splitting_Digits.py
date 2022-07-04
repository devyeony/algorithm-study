# #2 - LeetCode : 2160. Minimum Sum of Four Digit Number After Splitting Digits

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        first = num // 1000
        second = num % 1000 // 100
        third = num % 100 // 10
        fourth = num % 10
        nums = [first, second, third, fourth]
        nums.sort()
        return nums[0] * 10 + nums[1] * 10 + nums[2] + nums[3]


sol = Solution()
print(sol.minimumSum(2932))
print(sol.minimumSum(4009))
