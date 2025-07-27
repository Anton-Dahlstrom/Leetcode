class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n-1):
            if nums[i] == nums[i-1]:
                continue
            l, r = i-1, i+1
            while l >= 0 and nums[l] == nums[i]:
                l -= 1
            while r < n and nums[r] == nums[i]:
                r += 1
            if i >= 0 and r < n:
                if nums[l] < nums[i] and nums[r] < nums[i]:
                    res += 1
                elif nums[l] > nums[i] and nums[r] > nums[i]:
                    res += 1
        return res


nums = [2, 4, 1, 1, 6, 5]
output = 3


obj = Solution()
res = obj.countHillValley(nums)
print(res)
print(output)
print(res == output)
