class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 2
        cur = 2
        for i in range(2, n):
            if nums[i] == nums[i-1] + nums[i-2]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 2
        return res


nums = [5, 2, 7, 9, 16]
output: 5


obj = Solution()
res = obj.longestSubarray(nums)
print(res)
print(output)
print(res == output)
