# #13 - LeetCode : 1769. Minimum Number of Operations to Move All Balls to Each Box
from typing import List


# 1차 시도 : Time Limit Exceeded
class Solution1:
    def minOperations(self, boxes: str) -> List[int]:
        count_list: List[int] = [0] * len(boxes)
        for i in range(0, len(boxes)):
            count: int = 0
            for j in range(0, len(boxes)):
                if i != j and boxes[j] == '1':
                    count += abs(i-j)
            count_list[i] = count
        return count_list


# 2차 시도 : ing
class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        count_list: List[int] = [0] * len(boxes)
        return count_list


sol = Solution2()
print(sol.minOperations("110"))
print(sol.minOperations("001011"))