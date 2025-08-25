class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        inc = True
        cnt = 0
        if nums[1] < nums[0]:
            return False

        for i in range(1, n):
            if nums[i] > nums[i-1] and not inc:
                inc = True
                cnt += 1
            elif nums[i] < nums[i-1] and inc:
                inc = False
                cnt += 1
            if nums[i] == nums[i-1] or cnt > 2:
                return False
        return cnt == 2


nums = [6, 7, 5, 1]
output = False

nums = [4, 1, 5, 2, 3]
output = False

obj = Solution()
res = obj.isTrionic(nums)
print(res)
print(output)
print(res == output)
