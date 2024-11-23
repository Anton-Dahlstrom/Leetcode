from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return

        def dfs(l, r):
            if l > r:
                return
            mid = r-((r-l)//2)
            node = TreeNode(val=nums[mid])
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node

        return dfs(0, len(nums)-1)


nums = [-10, -3, 0, 5, 9]

obj = Solution()
res = obj.sortedArrayToBST(nums)
print(res)
