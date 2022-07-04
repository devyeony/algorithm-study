# #21 - LeetCode : 1561. Maximum Number of Coins You Can Get
from typing import List

# 3487 ms
class Solution1:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer: int = 0
        while len(piles) > 0:
            piles.pop()
            answer += piles.pop()
            piles.pop(0)
        return answer

# 652 ms
class Solution2:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start_idx: int = len(piles) // 3
        answer: int = 0
        for i in range(start_idx, len(piles), 2):
            answer += piles[i]
        return answer
