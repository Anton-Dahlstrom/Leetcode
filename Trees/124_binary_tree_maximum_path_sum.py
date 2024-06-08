from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# You can keep going up and combining a node by only using the value of its left or right subtree.
# If you use the sum from both the left and right subtree the node will have to be the root of
# the solution
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.largest = float("-inf")

        def Dfs(node):
            total = node.val
            leftSum = 0
            rightSum = 0
            if node.left:
                leftSum = Dfs(node.left)
                if leftSum > 0:
                    total += leftSum
            if node.right:
                rightSum = Dfs(node.right)
                if rightSum > 0:
                    total += rightSum
            self.largest = max(self.largest, total)
            largestSide = max(leftSum, rightSum)
            if largestSide > 0:
                return largestSide + node.val
            return node.val
        Dfs(root)
        return self.largest


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

obj = Solution()
res = obj.maxPathSum(root)
print(res)
