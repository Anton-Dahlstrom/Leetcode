class Solution:
    def maxSum(self, nums: list[int]) -> int:
        added = set()
        start = max(nums)
        added.add(start)
        res = start
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] not in added:
                added.add(nums[i])
                res += nums[i]
        return res


nums = [1, 2, 3, 4, 5]
output = 15

obj = Solution()
res = obj.maxSum(nums)
print(res)
print(output)
print(res == output)
