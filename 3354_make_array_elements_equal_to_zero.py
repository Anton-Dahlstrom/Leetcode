class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        right = sum(nums)
        left = 0
        for i in range(n):
            left += nums[i]
            right -= nums[i]
            if not nums[i]:
                if left == right:
                    res += 2
                elif abs(left-right) == 1:
                    res += 1
            if left > right+1:
                break
        return res


nums = [1, 0, 2, 0, 3]
output = 2


obj = Solution()
res = obj.countValidSelections(nums)
print(res)
print(output)
print(res == output)
