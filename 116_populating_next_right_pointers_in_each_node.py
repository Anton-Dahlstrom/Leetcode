from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return
        arr = [root]
        temp = []
        while arr:
            prev = None
            for node in arr:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if prev:
                    prev.next = node
                prev = node
            arr = temp
            temp = []
        return root
