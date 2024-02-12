from typing import Optional

root = [4, 2, 7, 1, 3, 6, 9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur:
                if cur.right or cur.left:
                    l = cur.left
                    r = cur.right
                    stack.append(l)
                    stack.append(r)
                    cur.right = l
                    cur.left = r
        return root
