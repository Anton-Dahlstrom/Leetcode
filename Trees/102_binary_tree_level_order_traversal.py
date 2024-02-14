from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [[0, root]]
        result = []
        while stack:
            node = stack.pop(0)
            if not node[1]:
                continue
            stack.append([node[0]+1, node[1].left])
            stack.append([node[0]+1, node[1].right])
            if len(result) <= node[0]:
                result.append([node[1].val])
            else:
                result[node[0]].append(node[1].val)
        return result
