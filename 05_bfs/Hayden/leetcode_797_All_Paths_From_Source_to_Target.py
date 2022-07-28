# #35 - LeetCode : 797. All Paths From Source to Target

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answers = []
        paths = [[0]]
        while paths:
            temp = []
            for path in paths:
                if path[-1] == len(graph) - 1:  # 마지막 노드일 때
                    answers.append(path)
                    continue
                for node in graph[path[-1]]:
                    temp.append(path + [node])
            paths = temp
        return answers


graph = [[1, 2], [3], [3], []]
sol = Solution()
print(sol.allPathsSourceTarget(graph))

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(sol.allPathsSourceTarget(graph))
