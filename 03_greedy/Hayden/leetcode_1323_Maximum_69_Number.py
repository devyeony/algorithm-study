# #21 - LeetCode : 1323. Maximum 69 Number
from typing import List


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str: str = str(num)
        index: int = 0
        for idx, val in enumerate(num_str):
            if val != '9':
                index = idx
                break
        num_list: List[str] = list(num_str)
        num_list[index] = '9'
        return ''.join(num_list)


sol = Solution()
print(sol.maximum69Number(9669))
print(sol.maximum69Number(9996))
print(sol.maximum69Number(9999))
