class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        res = 10**5 * nums[-1] * nums[-2]
        return abs(res)


nums = [-4, -2, -1, -3]
output = 1200000

obj = Solution()
res = obj.maxProduct(nums)
print(res)
print(output)
print(res == output)
