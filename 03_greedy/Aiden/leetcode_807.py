class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = [max(row) for row in grid]
        colum = [max(colum) for colum in zip(*grid)]
        sum = 0

        for i1, val1 in enumerate(row):
            for i2, val2 in enumerate(colum):
                sum+=(min(val1, val2)-grid[i1][i2])
        return sum