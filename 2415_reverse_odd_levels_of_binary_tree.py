from typing import Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        root.left, root.right = root.right, root.left
        arr = [root.left, root.right]
        steps = 1
        while arr:
            temp = deque()
            r = len(arr)//2
            l = r-1
            if not arr[l].left:
                break

            while l >= 0:
                if steps % 2:
                    arr[l].left, arr[l].right, arr[r].left, arr[r].right = arr[r].left, arr[r].right, arr[l].left, arr[l].right
                else:
                    arr[l].left, arr[l].right, arr[r].left, arr[r].right = arr[r].right, arr[r].left, arr[l].right, arr[l].left
                temp.appendleft(arr[l].right)
                temp.appendleft(arr[l].left)
                temp.append(arr[r].left)
                temp.append(arr[r].right)
                l -= 1
                r += 1
            arr = temp
            steps += 1
        return root
