# #30 - LeetCode : 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer: int = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.searchTree(root, -(10 ** 4))
        return self.answer

    def searchTree(self, node: TreeNode, max_value: int):
        if node is None:
            return

        if node.val >= max_value:
            self.answer += 1
            max_value = node.val

        self.searchTree(node.left, max_value)
        self.searchTree(node.right, max_value)


sol = Solution()
treeNode1: TreeNode = TreeNode(3, TreeNode(1, TreeNode(3, None, None), None), TreeNode(4, TreeNode(1, None, None), TreeNode(5, None, None)))
print(sol.goodNodes(treeNode1))

sol = Solution()
treeNode2: TreeNode = TreeNode(3, TreeNode(3, TreeNode(4, None, None), TreeNode(2, None, None)), None)
print(sol.goodNodes(treeNode2))

sol = Solution()
treeNode3: TreeNode = TreeNode(1, None, None)
print(sol.goodNodes(treeNode3))
