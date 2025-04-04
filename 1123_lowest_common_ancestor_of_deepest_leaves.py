from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(depth, node, parent):
            if not node:
                return (depth, parent)
            depth += 1
            d1, n1 = dfs(depth, node.left, node)
            d2, n2 = dfs(depth, node.right, node)
            if d1 == d2:
                return (d1, node)
            if d1 > d2:
                return (d1, n1)
            if d1 < d2:
                return (d2, n2)

        maxdepth, node = dfs(0, root, root)
        return node
