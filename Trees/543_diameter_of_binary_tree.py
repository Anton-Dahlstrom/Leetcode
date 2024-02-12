from typing import Optional

root = [1, 2, 3, 4, 5]
Output: 3


root = [2, 3, None, 1]
Output: 2

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        largest = 0
        while stack:
            l = 0
            r = 0
            node = stack.pop(0)
            if node.left:
                l = self.findDepth(node.left)
                stack.append(node.left)
            if node.right:
                r = self.findDepth(node.right)
                stack.append(node.right)
            largest = max(largest, l + r)
        return largest

    def findDepth(self, node):
        l = 0
        r = 0
        if node.left:
            l = self.findDepth(node.left)
        if node.right:
            r = self.findDepth(node.right)
        return max(l, r) + 1
