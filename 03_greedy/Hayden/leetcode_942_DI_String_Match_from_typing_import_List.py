# #21 - LeetCode : 942. DI String Match
from typing import List
from collections import deque


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm: List[int] = deque()
        for i in range(0, len(s) + 1):
            perm.append(i)
        answer: List[int] = []
        for i in s:
            if i == 'I':
                answer.append(perm.popleft())
            if i == 'D':
                answer.append(perm.pop())
        answer.append(perm.pop())
        return answer


sol = Solution()
print(sol.diStringMatch('IDID'))
print(sol.diStringMatch('III'))
print(sol.diStringMatch('DDI'))
