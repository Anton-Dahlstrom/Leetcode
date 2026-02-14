from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = nums[1]
            if colors[0] != colors[1]:
                dp[1] += dp[0]
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            if colors[i] != colors[i-1]:
                dp[i] = max(dp[i], dp[i-1] + nums[i])
        return max(dp[0], dp[-1])


nums = [1, 4, 3, 5]
colors = [1, 1, 2, 2]
output = 9

obj = Solution()
res = obj.rob(nums, colors)
print(res)
print(output)
print(res == output)
