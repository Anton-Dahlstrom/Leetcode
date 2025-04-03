class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        prefix = [0]*n
        curmax = 0
        for i in range(n-1, -1, -1):
            curmax = max(curmax, nums[i])
            prefix[i] = curmax
        lmax = nums[0]
        for i in range(1, n-1):
            res = max(res, (lmax - nums[i]) * prefix[i+1])
            lmax = max(lmax, nums[i])
        return res


nums = [8, 6, 3, 13, 2, 12, 19, 5, 19, 6, 10, 11, 9]
output = 266

obj = Solution()
res = obj.maximumTripletValue(nums)
print(res)
print(output)
print(res == output)
