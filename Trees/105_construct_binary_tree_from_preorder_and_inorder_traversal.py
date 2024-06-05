from typing import Optional

# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# preorder = [1, 2]
# inorder = [2, 1]
# output = [1, 2]

# preorder = [1, 2]
# inorder = [1, 2]
# output = [1, 2]

preorder = [1, 2, 3]
inorder = [3, 2, 1]
output = [1, 2, 3]

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
            if not curNodes:
                curNodes = nextNodes
                nextNodes = []
            cur = curNodes.pop(0)
            curInorderIndex = self.Find(cur.val, start, inorder)
            print(curInorderIndex)
            left = TreeNode(preorder[i])
            leftIndex = self.Find(left.val, curInorderIndex, inorder)
            # Ugly solution
            while leftIndex > curInorderIndex:
                if not curNodes:
                    cur.right = left
                    return root
                cur = curNodes.pop(0)
                curInorderIndex = self.Find(cur.val, curInorderIndex, inorder)

            cur.left = left
            nextNodes.append(left)
            if i < len(preorder)-1:
                right = TreeNode(preorder[i+1])
                cur.right = right
                nextNodes.append(right)
            i += 2
        return root
        # cur = root
        # while cur:
        #     print(cur.val)
        #     cur = cur.left
        # cur = root
        # while cur:
        #     print(cur.val)
        #     cur = cur.right
        # print(curNodes)

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
