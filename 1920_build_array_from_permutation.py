class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[nums[i]]
        return res


nums = [0, 2, 1, 5, 3, 4]
output = [0, 1, 2, 4, 5, 3]

obj = Solution()
res = obj.buildArray(nums)
print(res)
print(output)
print(res == output)
