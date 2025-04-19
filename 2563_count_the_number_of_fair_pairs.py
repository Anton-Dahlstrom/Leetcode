class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        res = 0
        while l < r:
            while l < r and nums[l] + nums[r] > upper:
                r -= 1
            if nums[l] + nums[r] < lower:
                l += 1
                continue
            if r <= l:
                break
            templ, tempr = l+1, r
            while templ < tempr:
                mid = templ + ((tempr-templ)//2)
                if nums[mid] + nums[l] < lower:
                    templ = mid + 1
                else:
                    tempr = mid
            res += r-tempr+1
            l += 1
        return res


nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
output = 6


obj = Solution()
res = obj.countFairPairs(nums, lower, upper)
print(res)
print(output)
print(res == output)
