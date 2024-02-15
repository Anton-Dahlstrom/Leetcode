from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        stack = [[0, root]]
        result = []

        while stack:
            node = stack.pop(0)
            if not node[1]:
                continue
            if len(result) <= node[0]:
                result.append(node[1].val)
            stack.append([node[0]+1, node[1].right])
            stack.append([node[0]+1, node[1].left])
        return result
