class Solution:
    def maximumPossibleSize(self, nums: list[int]) -> int:
        prev = -1
        n = len(nums)
        res = n
        for i in range(n):
            if nums[i] < prev:
                res -= 1
            else:
                prev = nums[i]
        return res


nums = [4, 2, 5, 3, 5]
output = 3

obj = Solution()
res = obj.maximumPossibleSize(nums)
print(res)
print(output)
print(res == output)
