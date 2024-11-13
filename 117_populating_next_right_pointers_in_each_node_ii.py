# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return

        arr = [root]
        temp = []
        while arr:
            prev = None
            for cur in arr:
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                if prev:
                    prev.next = cur
                prev = cur
            arr = temp
            temp = []
        return root
