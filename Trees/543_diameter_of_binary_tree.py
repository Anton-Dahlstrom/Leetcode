from typing import Optional

root = [1, 2, 3, 4, 5]
Output: 3

# Definition for a binary tree node.

root = [2, 3, None, 1]
Output: 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 0, 0, 0]]
        left = 0
        right = 0
        depth = 0
        while stack:
            node = stack.pop(0)
            if node[0].left:
                stack.append([node[0].left, node[1]+1, node[2]-1, node[3]+1])
                left = max(left, node[1]+1)
            if node[0].right:
                right = max(right, node[2]+1)
                stack.append([node[0].right, node[1]-1, node[2]+1, node[3]+1])
            depth = max(depth, node[3])
        return max(left + right, depth)


test = [1, 2, None, 5, 6, 7, 8]
while test:
    asd = test.pop()
    print(asd)
