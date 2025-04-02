class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res


nums = [12, 6, 1, 2, 7]
output = 77

obj = Solution()
res = obj.maximumTripletValue(nums)
print(res)
print(output)
print(res == output)
