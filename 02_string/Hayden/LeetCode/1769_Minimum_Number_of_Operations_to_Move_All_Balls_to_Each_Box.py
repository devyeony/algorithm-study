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


# 2차 시도 : 76 ms
class Solution2(object):
    def minOperations(self, boxes):
        all_box_count, all_move = 0, 0
        ret = [0] * len(boxes)
        for i in range(len(boxes)):
            all_move += all_box_count
            if boxes[i] == '1':
                all_box_count += 1
            ret[i] += all_move

        all_box_count, all_move = 0, 0
        for i in range(len(boxes) - 1, -1, -1):
            all_move += all_box_count
            if boxes[i] == '1':
                all_box_count += 1
            ret[i] += all_move
        return ret


sol = Solution2()
print(sol.minOperations("110"))
print(sol.minOperations("001011"))
