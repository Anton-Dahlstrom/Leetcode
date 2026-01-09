from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.deepnodes = 0
        self.root = None

        def getDepth(node):
            maxdepth = 0
            if node.left:
                maxdepth = max(maxdepth, getDepth(node.left))
            if node.right:
                maxdepth = max(maxdepth, getDepth(node.right))
            return maxdepth + 1

        self.depth = getDepth(root)

        def dfs(node, depth):
            deepnodes = 0
            if depth == self.depth:
                deepnodes += 1
            if node.left:
                deepcount = dfs(node.left, depth+1)
                deepnodes += deepcount

            if node.right:
                deepcount = dfs(node.right, depth+1)
                deepnodes += deepcount

            if deepnodes > self.deepnodes:
                self.deepnodes = deepnodes
                self.root = node
            return deepnodes

        dfs(root, 1)
        return self.root
