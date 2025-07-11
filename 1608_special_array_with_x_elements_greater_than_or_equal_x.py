class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[-i-1] < i and nums[-i] >= i:
                return i
        if nums[-n] >= n:
            return n
        return -1


nums = [3, 5]
output = 2


obj = Solution()
res = obj.specialArray(nums)
print(res)
print(output)
print(res == output)
