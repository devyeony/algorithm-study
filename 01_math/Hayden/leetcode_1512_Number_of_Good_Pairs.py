class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        nums_length = len(nums)
        for i in range(0, nums_length - 1):
            for j in range(i + 1, nums_length):
                if nums[i] == nums[j]:
                    count += 1
        return count


sol = Solution()
print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4
print(sol.numIdenticalPairs([1, 1, 1, 1]))  # 6
print(sol.numIdenticalPairs([1, 2, 3]))  # 0
