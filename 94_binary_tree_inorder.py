from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        if not root:
            return res

        def search(node):
            if node.left:
                search(node.left)
            res.append(node.val)
            if node.right:
                search(node.right)

        search(root)
        return res
