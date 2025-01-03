class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix = [0] * (len(nums)+1)
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1] + prefix[i-1]
        res = 0
        for i in range(1, len(prefix)-1):
            if prefix[i] >= (prefix[len(prefix)-1]) - prefix[i]:
                res += 1
        return res


nums = [10, 4, -8, 7]
output = 2

obj = Solution()
res = obj.waysToSplitArray(nums)
print(res)
print(output)
print(res == output)
