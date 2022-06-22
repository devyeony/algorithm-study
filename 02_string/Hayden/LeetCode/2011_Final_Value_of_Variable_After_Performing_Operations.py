# #13 - LeetCode : 2011. Final Value of Variable After Performing Operations
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum: int = 0
        for operation in operations:
            if '--' in operation:
                sum -= 1
            if '++' in operation:
                sum += 1
        return sum


sol = Solution()
print(sol.finalValueAfterOperations(["--X", "X++", "X++"]))
print(sol.finalValueAfterOperations(["++X", "++X", "X++"]))
print(sol.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
