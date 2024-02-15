from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = [root]
        array = []
        while nodes:
            node = nodes.pop()
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

            if not array:
                array.append(node.val)
                continue
            if len(array) < k:
                if node.val > array[-1]:
                    array.append(node.val)
                    continue
                else:
                    for i, val in enumerate(array):
                        if node.val < val:
                            array.insert(i, node.val)
                            break
            else:
                for i, val in enumerate(array):
                    if node.val < val:
                        array.insert(i, node.val)
                        break
                if len(array) > k:
                    array.pop(-1)

        return array[-1]
