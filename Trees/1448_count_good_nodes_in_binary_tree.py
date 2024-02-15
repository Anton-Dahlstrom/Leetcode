# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root.val, root]]
        result = 0
        while stack:
            node = stack.pop()
            if not node[1]:
                continue
            if node[1].val >= node[0]:
                result += 1
            largest = max(node[0], node[1].val)
            stack.append([largest, node[1].right])
            stack.append([largest, node[1].left])
        return result
