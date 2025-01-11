class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        res = 0
        left = nums[0][1]
        for i in range(1, len(nums)):
            res = max(nums[i][1] - left, res)
            left = min(left, nums[i][1])
        return res


nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
output = 7

obj = Solution()
res = obj.maxWidthRamp(nums)
print(res)
print(output)
print(res == output)
