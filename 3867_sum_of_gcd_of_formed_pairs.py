from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixMax = [0]*n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(nums[i], prefixMax[i-1])
        prefixGcd = [0]*n
        for i in range(n):
            prefixGcd[i] = gcd(prefixMax[i], nums[i])
        prefixGcd.sort()
        l, r = 0, n-1
        res = 0
        while l < r:
            res += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return res


nums = [2, 6, 4]
output = 2

obj = Solution()
res = obj.gcdSum(nums)
print(res)
print(output)
print(res == output)
