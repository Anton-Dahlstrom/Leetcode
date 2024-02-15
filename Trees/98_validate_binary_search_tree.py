from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, None, None]]

        while stack:
            node = stack.pop()
            if node[1] is not None:
                if node[0].val >= node[1]:
                    return False
            if node[2] is not None:
                if node[0].val <= node[2]:
                    return False

            if node[0].left:
                stack.append([node[0].left, node[0].val, node[2]])
            if node[0].right:
                stack.append([node[0].right, node[1], node[0].val])
        return True
