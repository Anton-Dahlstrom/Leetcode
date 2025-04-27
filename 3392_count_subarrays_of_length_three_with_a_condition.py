class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):
            if ((nums[i] + nums[i+2]) * 2) == nums[i+1]:
                res += 1
        return res


nums = [1, 2, 1, 4, 1]
output = 1

obj = Solution()
res = obj.countSubarrays(nums)
print(res)
print(output)
print(res == output)
