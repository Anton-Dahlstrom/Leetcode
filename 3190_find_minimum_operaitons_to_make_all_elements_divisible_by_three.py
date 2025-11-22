class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            if num % 3:
                res += 1
        return res


nums = [1, 2, 3, 4]
output = 3

obj = Solution()
res = obj.minimumOperations(nums)
print(res)
print(output)
print(res == output)
