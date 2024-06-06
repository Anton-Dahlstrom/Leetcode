from typing import Optional

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

# preorder = [1, 2]
# inorder = [2, 1]
# output = [1, 2]

# preorder = [1, 2]
# inorder = [1, 2]
# output = [1, 2]

preorder = [1, 2, 3]
inorder = [3, 2, 1]
output = [1, 2, 3]

# preorder = [1, 2, 3]
# inorder = [2, 3, 1]
# output = [1, 2, 3]


preorder = [1, 2, 3]
inorder = [1, 2, 3]
output = [1, 2, 3]

preorder = [3, 1, 2, 4]
inorder = [1, 2, 3, 4]
output = [3, 1, 2, 4]
#   3
# 1    4
#  2
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Use preorder to determine the order which nodes are created.
# The inorder exists only to determine the sequence of the preorder nodes.
# Let's first create a solution that works if the tree is symmetrical.


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        curNodes = [root]  # Keep track of nodes for Bfs.
        nextNodes = []
        i = 1
        start = len(preorder)//2
        while i < len(preorder):
            stop = False
            if not curNodes:
                curNodes = nextNodes
                nextNodes = []
            cur = curNodes.pop(0)
            curInorderIndex = self.Find(cur.val, start, inorder)
            left = TreeNode(preorder[i])
            leftInorderIndex = self.Find(left.val, curInorderIndex, inorder)
            # Ugly solution
            while leftInorderIndex > curInorderIndex:
                if not curNodes:
                    cur.right = left
                    nextNodes.append(left)
                    stop = True
                    i += 1
                    break
                cur = curNodes.pop(0)
                curInorderIndex = self.Find(cur.val, curInorderIndex, inorder)
            if stop:
                continue
            cur.left = left
            nextNodes.append(left)
            if i < len(preorder)-1:
                right = TreeNode(preorder[i+1])
                rightInorderIndex = self.Find(
                    right.val, curInorderIndex, inorder)
                if rightInorderIndex > leftInorderIndex and rightInorderIndex > curInorderIndex:
                    cur.right = right
                    nextNodes.append(right)
                    i += 2
                    continue
                # elif rightInorderIndex > leftInorderIndex and rightInorderIndex < curInorderIndex:
                    # left.

            i += 1
        return root

    def Find(self, target: int, index: int, array: list):
        l = index
        r = index
        if array[index] == target:
            return index
        while l > 0 or r < len(array)-1:
            if l > 0:
                l -= 1
                if array[l] == target:
                    return l
            if r < len(array)-1:
                r += 1
                if array[r] == target:
                    return r


obj = Solution()
res = obj.buildTree(preorder, inorder)
print(res)
nodes = [res]
while nodes:
    cur = nodes.pop(0)
    print(cur.val)
    if cur.left:
        nodes.append(cur.left)
    if cur.right:
        nodes.append(cur.right)
print(res.left.right.right.val)
# print(res.right.val)
