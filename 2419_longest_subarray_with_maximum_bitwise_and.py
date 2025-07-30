class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        k = max(nums)
        l, r = 0, 0
        res == 0, 0
        while l < n:
            r = l
            while r < n and nums[r] == k:
                r += 1
            res = max(res, r-l)
            l = r+1
        return res


nums = [1, 2, 3, 3, 2, 2]
output = 2

obj = Solution()
res = obj.longestSubarray(nums)
print(res)
print(output)
print(res == output)
