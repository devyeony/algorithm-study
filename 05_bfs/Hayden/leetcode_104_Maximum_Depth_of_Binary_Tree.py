# #35 - LeetCode : 104. Maximum Depth of Binary Tree

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth: int = 0
        if root is None:
            return depth
        subtree_list: List[TreeNode] = [root]
        while len(subtree_list) > 0:
            subtree_size: int = len(subtree_list)
            for _ in range(0, subtree_size):
                current_tree: TreeNode = subtree_list.pop(0)
                if current_tree.left is not None:
                    subtree_list.append(current_tree.left)
                if current_tree.right is not None:
                    subtree_list.append(current_tree.right)
            depth += 1
        return depth


sol = Solution()
root1_left: Optional[TreeNode] = TreeNode(9, None, None)
root1_right: Optional[TreeNode] = TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))
root1: Optional[TreeNode] = TreeNode(3, root1_left, root1_right)
print(sol.maxDepth(root1))

root2: Optional[TreeNode] = TreeNode(1, None, TreeNode(2, None, None))
print(sol.maxDepth(root2))
