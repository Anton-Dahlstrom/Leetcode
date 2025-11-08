class Solution:
    def minMoves(self, nums: list[int]) -> int:
        tar = max(nums)
        res = 0
        for num in nums:
            res += tar-num
        return res


nums = [2, 1, 3]
output = 3

obj = Solution()
res = obj.minMoves(nums)
print(res)
print(output)
print(res == output)
