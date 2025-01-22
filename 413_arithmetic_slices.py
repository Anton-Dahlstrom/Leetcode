class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        l = 0
        r = 1
        res = 0
        diff = 0
        while r < len(nums):
            size = r-l
            if size == 1:
                diff = nums[l]-nums[r]
            else:
                if nums[r-1] - nums[r] == diff:
                    if size >= 2:
                        res += size - 1
                else:
                    l = r-1
                    continue
            r += 1
        return res


nums = [1, 2, 3, 4]
output = 3


obj = Solution()
res = obj.numberOfArithmeticSlices(nums)
print(res)
print(output)
print(res == output)
