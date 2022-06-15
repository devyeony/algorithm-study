# #13 - LeetCode : 1769. Minimum Number of Operations to Move All Balls to Each Box
from typing import List


# 1차 시도 : 8356 ms
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


# 2차 시도 : 130 ms
class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        first_count = 0  # count_list[0]에 들어갈 첫번째 카운팅
        ones = 0  # 1의 총 개수
        for i, box in enumerate(boxes):
            if box == "1":
                first_count += i
                ones += 1
        count_list = [0] * len(boxes)
        visited = 0  # 1이 나온 횟수
        for i in range(len(boxes)):
            if i == 0:
                count_list[0] = first_count
            else:
                count_list[i] = count_list[i - 1] - (ones - visited) + visited
            if boxes[i] == "1":
                visited += 1
        return count_list


sol = Solution2()
print(sol.minOperations("110"))
print(sol.minOperations("001011"))
