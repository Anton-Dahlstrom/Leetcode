class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0] == nums[-1]:
            return 0
        n = len(nums)
        res = sum(nums[1:])
        res -= (n-1) * nums[0]
        return res
