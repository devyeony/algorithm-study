# #21 - LeetCode - 1529. Minimum Suffix Flips

class Solution:
    def minFlips(self, target: str) -> int:
        prev_num: str = target[0]
        count: int = (1 if prev_num == '1' else 0)
        for i in range(1, len(target)):
            if target[i] != prev_num:
                count += 1
                prev_num = target[i]
        return count

sol = Solution()
print(sol.minFlips('10111'))
print(sol.minFlips('101'))
print(sol.minFlips('00000'))
