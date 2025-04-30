class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if not len(str(nums[i])) % 2:
                res += 1
        return res


nums = [12, 345, 2, 6, 7896]
output = 2

obj = Solution()
res = obj.findNumbers(nums)
print(res)
print(output)
print(res == output)
