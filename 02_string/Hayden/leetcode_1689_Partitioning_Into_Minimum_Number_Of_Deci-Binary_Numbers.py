# #13 - LeetCode : 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        max_num: int = int(n[0])
        for num in n:
            if int(num) > max_num:
                max_num = int(num)
        return max_num

sol = Solution()
print(sol.minPartitions("32"))
print(sol.minPartitions("82734"))
print(sol.minPartitions("27346209830709182346"))