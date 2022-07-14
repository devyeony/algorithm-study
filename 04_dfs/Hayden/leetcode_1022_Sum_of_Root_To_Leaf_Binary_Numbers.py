# #30 - LeetCode : 1022. Sum of Root To Leaf Binary Numbers
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.sum = 0
        self.dfs(root, str(root.val))
        return self.sum

    def dfs(self, node: Optional[TreeNode], current_str: str):
        print("current_str : ", current_str)
        if not node.left and not node.right:
            self.sum += int(current_str, 2)
            print("========================")
            return

        if node.left:
            self.dfs(node.left, current_str + str(node.left.val))
        if node.right:
            self.dfs(node.right, current_str + str(node.right.val))


# input
leaf1: Optional[TreeNode] = TreeNode(0, None, None)
leaf2: Optional[TreeNode] = TreeNode(1, None, None)
middle1: Optional[TreeNode] = TreeNode(0, leaf1, leaf2)

leaf3: Optional[TreeNode] = TreeNode(0, None, None)
leaf4: Optional[TreeNode] = TreeNode(1, None, None)
middle2: Optional[TreeNode] = TreeNode(1, leaf3, leaf4)

root: Optional[TreeNode] = TreeNode(1, middle1, middle2)

# run
sol = Solution()
print(sol.sumRootToLeaf(root))
