class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0]*m for _ in range(n)]
        res = float("-inf")
        for i in range(n):
            for j in range(m):
                cur = nums1[i] * nums2[j]
                res = max(res, cur)
                if i and j:
                    cur += dp[i-1][j-1]
                dp[i][j] = max(cur, dp[i-1][j], dp[i][j-1])
        if res < 0:
            return res
        return dp[n-1][m-1]


nums2 = [3, 0, -6]
nums1 = [2, 1, -2, 5]
output = 18


obj = Solution()
res = obj.maxDotProduct(nums1, nums2)
print(res)
print(output)
print(res == output)
