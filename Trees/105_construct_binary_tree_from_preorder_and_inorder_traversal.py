from typing import Optional

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        rootInorderIndex = self.Find(root.val, len(preorder)//2, inorder)
        i = 1
        while i < len(preorder):
            search = True
            cur = root
            curInorderIndex = rootInorderIndex
            next = TreeNode(preorder[i])
            nextInorderIndex = self.Find(next.val, rootInorderIndex, inorder)
            while search:
                while nextInorderIndex < curInorderIndex:
                    if not cur.left:
                        cur.left = next
                        search = False
                        continue
                    else:
                        cur = cur.left
                        curInorderIndex = self.Find(
                            cur.val, curInorderIndex, inorder)

                while nextInorderIndex > curInorderIndex:
                    if not cur.right:
                        cur.right = next
                        search = False
                        continue
                    else:
                        cur = cur.right
                        curInorderIndex = self.Find(
                            cur.val, curInorderIndex, inorder)
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
nodes = [res]
while nodes:
    cur = nodes.pop(0)
    print(cur.val)
    if cur.left:
        nodes.append(cur.left)
    if cur.right:
        nodes.append(cur.right)
