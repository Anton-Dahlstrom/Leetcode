class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = float("-inf")
        best = {0: 0}
        cur = 0
        for i in range(k-1):
            cur += nums[i]
            best[i+1] = cur
        for i in range(k-1, n):
            cur += nums[i]
            rem = (i+1) % k
            res = max(res, cur-best[rem])
            best[rem] = min(best[rem], cur)
        return res


nums = [-5, 1, 2, -3, 4]
k = 2
output = 4

obj = Solution()
res = obj.maxSubarraySum(nums, k)
print(res)
print(output)
print(res == output)
