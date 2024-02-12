from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            if node.val != subRoot.val:
                continue
            if self.compare(node, subRoot):
                return True

    def compare(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        left = self.compare(root.left, subRoot.left)
        right = self.compare(root.right, subRoot.right)

        if not left or not right:
            return False
        return True
