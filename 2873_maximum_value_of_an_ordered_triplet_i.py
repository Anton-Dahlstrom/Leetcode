class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        prefix = [0]*n
        curmax = 0
        for i in range(n-1, -1, -1):
            curmax = max(curmax, nums[i])
            prefix[i] = curmax
        # keep track of biggest val left
        # prefix for biggest val right
        lmax = nums[0]
        for i in range(1, n-1):
            res = max(res, (lmax - nums[i]) * prefix[i+1])
            lmax = max(lmax, nums[i])
        return res


nums = [12, 6, 1, 2, 7]
output = 77

obj = Solution()
res = obj.maximumTripletValue(nums)
print(res)
print(output)
print(res == output)
