class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        res = 0
        prevmin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prevmin:
                prevmin = nums[i]
            else:
                res = max(res, nums[i] - prevmin)
        if not res:
            res = -1
        return res


nums = [7, 1, 5, 4]
output = 4

obj = Solution()
res = obj.maximumDifference(nums)
print(res)
print(output)
print(res == output)
