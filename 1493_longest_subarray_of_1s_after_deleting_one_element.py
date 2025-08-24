class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        prevsum = 0
        cursum = 0
        for i in range(n):
            if nums[i]:
                cursum += 1
            else:
                prevsum = cursum
                cursum = 0
            res = max(res, prevsum+cursum)
        res = min(res, n-1)
        return res


nums = [1, 1, 0, 1]
output = 3

obj = Solution()
res = obj.longestSubarray(nums)
print(res)
print(output)
print(res == output)
