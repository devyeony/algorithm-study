# #30 - LeetCode : 1302. Deepest Leaves Sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return


# input1
leaf1: Optional[TreeNode] = TreeNode(7, None, None)
parent1: Optional[TreeNode] = TreeNode(4, leaf1, None)
parent2: Optional[TreeNode] = TreeNode(5, None, None)
grand_parent1: Optional[TreeNode] = TreeNode(2, parent1, parent2)

leaf2: Optional[TreeNode] = TreeNode(8, None, None)
parent3: Optional[TreeNode] = TreeNode(6, None, leaf2)
grand_parent2: Optional[TreeNode] = TreeNode(3, None, parent3)

root1: Optional[TreeNode] = TreeNode(1, grand_parent1, grand_parent2)

# run1
sol = Solution()
print(sol.deepestLeavesSum(root1))

