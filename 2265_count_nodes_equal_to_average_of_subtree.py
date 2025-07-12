# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            count, total = 1, node.val
            if node.left:
                lcount, lsum = dfs(node.left)
                count += lcount
                total += lsum

            if node.right:
                rcount, rsum = dfs(node.right)
                count += rcount
                total += rsum

            if total//count == node.val:
                self.res += 1
            return count, total

        dfs(root)
        return self.res


root = [4, 8, 5, 0, 1, None, 6]
output = 5

obj = Solution()
res = obj.averageOfSubtree(root)
print(res)
print(output)
print(res == output)
