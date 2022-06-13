# #13 - LeetCode : 1859_Sorting_the_Sentence.py
from mypy.api import List


class Solution:
    def sortSentence(self, s: str) -> str:
        s_split: List[str] = s.split(" ")
        sentence_list: List[str] = [""] * (len(s_split))
        for i in range(0, len(s_split)):
            s_element: str = s_split[i]
            seq: int = int(s_element[len(s_element)-1])
            sentence_list[seq-1] = s_element[0:-1]
        return " ".join(sentence for sentence in sentence_list)


sol = Solution()
print(sol.sortSentence("is2 sentence4 This1 a3"))
