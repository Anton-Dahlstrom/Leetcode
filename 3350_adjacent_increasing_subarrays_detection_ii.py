class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        res = 1
        prev = 0
        cur = 0
        for i in range(n):
            if nums[i] <= nums[i-1]:
                prev = cur
                cur = 0
            cur += 1
            res = max(res, cur//2, min(prev, cur))
        return res


nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
output = 3


obj = Solution()
res = obj.maxIncreasingSubarrays(nums)
print(res)
print(output)
print(res == output)
