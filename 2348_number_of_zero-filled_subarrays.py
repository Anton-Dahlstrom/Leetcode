class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        l, r = 0, 0
        while l < n:
            if nums[l]:
                l += 1
                continue
            r = l+1
            while r < n and not nums[r]:
                r += 1
            res += ((r-l+1)/2) * (r-l)
            l = r+1
        return int(res)


nums = [1, 3, 0, 0, 2, 0, 0, 4]
output = 6

obj = Solution()
res = obj.zeroFilledSubarray(nums)
print(res)
print(output)
print(res == output)
