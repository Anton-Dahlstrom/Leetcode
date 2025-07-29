class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        res = 0
        while l < r:
            res += nums[r-1]
            l += 1
            r -= 2
        return res


nums = [2, 1, 3, 2, 1, 3]
output = 5

obj = Solution()
res = obj.maximumMedianSum(nums)
print(res)
print(output)
print(res == output)
