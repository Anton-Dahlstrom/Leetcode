class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        decreasing = 1
        increasing = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                increasing += 1
                res = max(res, increasing)
                decreasing = 1
            elif nums[i-1] > nums[i]:
                decreasing += 1
                res = max(res, decreasing)
                increasing = 1
            else:
                increasing = 1
                decreasing = 1

        return res


nums = [1, 4, 3, 3, 2]
output = 2

obj = Solution()
res = obj.longestMonotonicSubarray(nums)
print(res)
print(output)
print(res == output)
