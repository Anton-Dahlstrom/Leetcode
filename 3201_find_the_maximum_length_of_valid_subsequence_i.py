class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        n = len(nums)
        evens = 0
        odds = 0
        alternating = 1
        cur = nums[0]
        for i in range(n):
            if nums[i] % 2:
                odds += 1
            else:
                evens += 1
            if i > 0 and (cur + nums[i]) % 2:
                alternating += 1
                cur = nums[i]
        return max(evens, odds, alternating)


nums = [1, 2, 1, 1, 2, 1, 2]
output = 6


obj = Solution()
res = obj.maximumLength(nums)
print(res)
print(output)
print(res == output)
