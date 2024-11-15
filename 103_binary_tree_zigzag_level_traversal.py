from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        arr = [root]
        temp = []
        res = []
        tempres = []
        order = True
        while arr:
            if order:
                for node in arr:
                    tempres.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                arr = temp
            else:
                for node in reversed(arr):
                    tempres.append(node.val)
                    if node.right:
                        temp.append(node.right)
                    if node.left:
                        temp.append(node.left)
                arr = reversed(temp)
            if tempres:
                res.append(tempres)
            tempres = []
            temp = []
            order = order == False
        return res
