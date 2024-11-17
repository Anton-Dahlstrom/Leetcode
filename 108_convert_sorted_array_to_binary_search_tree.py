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
        root = TreeNode(val=nums[0])
        prev = root
        for i in range(1, len(nums)):
            cur = TreeNode(nums[i])
            if i <= len(nums)//2:
                cur.left = prev
                root = cur
            else:
                prev.right = cur
            prev = cur
        return root


nums = [-10, -3, 0, 5, 9]

obj = Solution()
res = obj.singleNumber(nums)
print(res)
