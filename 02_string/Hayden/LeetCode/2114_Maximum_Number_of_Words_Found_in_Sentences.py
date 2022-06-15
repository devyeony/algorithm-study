# #13 - LeetCode : 2114. Maximum Number of Words Found in Sentences
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        if len(sentences) == 0:
            return 0

        max_count: int = sentences[0].count(" ") + 1
        for i in range(1, len(sentences)):
            if sentences[i].count(" ") + 1 > max_count:
                max_count = sentences[i].count(" ") + 1
        return max_count


sol = Solution()
print(sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(sol.mostWordsFound(["please wait", "continue to fight", "continue to win"]))
