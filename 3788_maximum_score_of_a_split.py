class Solution:
    def maximumScore(self, nums: list[int]) -> int:
        n = len(nums)
        suffix = [0]*n
        cur = float("inf")
        for i in range(n-1, -1, -1):
            cur = min(cur, nums[i])
            suffix[i] = cur

        prefix = 0
        res = float("-inf")
        for i in range(n-1):
            prefix += nums[i]
            res = max(res, prefix-suffix[i+1])
        return res


nums = [10, -1, 3, -4, -5]
output = 17

obj = Solution()
res = obj.maximumScore(nums)
print(res)
print(output)
print(res == output)
