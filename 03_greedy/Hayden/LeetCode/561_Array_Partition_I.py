# #21 - LeetCode : 561. Array Partition I
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        max: int = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            max += nums[i]
        return max


sol = Solution()
print(sol.arrayPairSum([1, 4, 3, 2]))
print(sol.arrayPairSum([6, 2, 6, 5, 1, 2]))
