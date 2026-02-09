from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.arr = []

        def dfs(node):
            if not node:
                return
            self.arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.arr.sort()

        def makeTree(left, right):
            mid = left + ((right-left)//2)
            node = TreeNode(self.arr[mid])
            if mid-1 >= left:
                node.left = makeTree(left, mid-1)
            if mid+1 <= right:
                node.right = makeTree(mid+1, right)
            return node

        return makeTree(0, len(self.arr)-1)
