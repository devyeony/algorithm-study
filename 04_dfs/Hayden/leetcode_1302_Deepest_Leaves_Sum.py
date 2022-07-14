# #30 - LeetCode : 1302. Deepest Leaves Sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.leaves_sum = 0
        self.max_depth = 0
        self.dfs(root, 1)
        return self.leaves_sum

    def dfs(self, node: Optional[TreeNode], depth: int):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.leaves_sum = node.val
            elif depth == self.max_depth:
                self.leaves_sum += node.val
        if node.left:
            self.dfs(node.left, depth + 1)
        if node.right:
            self.dfs(node.right, depth + 1)


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


# input2
leaf3: Optional[TreeNode] = TreeNode(9, None, None)
leaf4: Optional[TreeNode] = TreeNode(1, None, None)
leaf5: Optional[TreeNode] = TreeNode(4, None, None)
parent4: Optional[TreeNode] = TreeNode(2, leaf3, None)
parent5: Optional[TreeNode] = TreeNode(7, leaf4, leaf5)
grand_parent3: Optional[TreeNode] = TreeNode(7, parent4, parent5)

leaf6: Optional[TreeNode] = TreeNode(5, None, None)
parent6: Optional[TreeNode] = TreeNode(1, None, None)
parent7: Optional[TreeNode] = TreeNode(3, None, leaf6)
grand_parent4: Optional[TreeNode] = TreeNode(8, parent6, parent7)

root2: Optional[TreeNode] = TreeNode(6, grand_parent3, grand_parent4)

# run2
sol = Solution()
print(sol.deepestLeavesSum(root2))
