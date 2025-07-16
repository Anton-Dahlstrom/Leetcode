class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        i = 0
        for j in range(1, n):
            if nums[j] > nums[i]:
                i += 1
                res += 1
        return res


nums = [1, 3, 5, 2, 1, 3, 1]
output = 4

obj = Solution()
res = obj.maximizeGreatness(nums)
print(res)
print(output)
print(res == output)
