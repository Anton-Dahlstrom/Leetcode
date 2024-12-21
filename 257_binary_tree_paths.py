from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        res = []

        def dfs(node, string):
            if not string:
                string = str(node.val)
            else:
                string += "->" + str(node.val)
            if not node.left and not node.right:
                res.append(string)
                return
            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)
        if root:
            dfs(root, "")
        return res
