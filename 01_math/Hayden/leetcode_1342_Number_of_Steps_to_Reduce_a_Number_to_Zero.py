# #2 - LeetCode : 1342. Number of Steps to Reduce a Number to Zero

class Solution(object):
    count = 0
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 0:
            num = self.compute(num)
        return self.count

    def compute(self, num):
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        self.count += 1
        return num


sol = Solution()
print(sol.numberOfSteps(14))
