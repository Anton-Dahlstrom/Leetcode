from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        swap = []
        # Find a node that needs to be swapped

        def findNode(node, maxcap, mincap, parent):
            if node.val > maxcap or node.val < mincap:
                swap.append(parent, node, maxcap, mincap)
                print(node.val)
            if node.left:
                findNode(node.left, node.val, mincap, node)
            if node.right:
                findNode(node.right, maxcap, node.val, node)

        def swapNode(parent1, child1, parent2, child2):
            if parent1.left and parent1.left.val == child1.val:
                parent1.left = child2
            else:
                parent1.right = child2

            if parent2.left and parent2.left.val == child1.val:
                parent2.left = child1
            else:
                parent2.right = child1
            child1.left, child1.right, child2.left, child2.right = child2.left, child2.right, child1.left, child1.right

        # Find a node it can be swapped with
        def findSwap(node, maxcap, mincap, parent, val):
            if node.val == val:
                if node.left:
                    findSwap(node.left, maxcap, mincap, node)
                if node.right:
                    findSwap(node.right, maxcap, mincap, node)

            if val < maxcap and val > mincap:
                if node.val < swap[0][2] and node.val > swap[0][3]:
                    cur = parent
            if node.left:
                findSwap(node.left, node.val, mincap, node)
            if node.right:
                findSwap(node.right, maxcap, node.val, node)

        findNode(root, float("inf"), 0, None)
        if len(swap) > 1:
            swapNode(swap[0][0], swap[0][1], swap[1][0], swap[1][1])
            return
        findSwap(root, float("inf"), 0, None, swap[0][1].val)


# root = [1, 3, None, None, 2]
# output = [3, 1, None, None, 2]
# obj = Solution()
# res = obj.intToRoman(num)
# print(res)
# print(output)
# print(res == output)
