class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            odd = set()
            even = set()
            for j in range(i, n):
                if nums[j] % 2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(odd) == len(even):
                    res = max(res, j-i+1)
        return res


nums = [3, 2, 2, 5, 4]
output = 5


obj = Solution()
res = obj.longestBalanced(nums)
print(res)
print(output)
print(res == output)
