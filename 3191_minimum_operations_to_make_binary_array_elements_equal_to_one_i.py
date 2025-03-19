class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):
            if not nums[i]:
                nums[i] = 1
                res += 1
                for j in range(i+1, i+3):
                    if not nums[j]:
                        nums[j] = 1
                    else:
                        nums[j] = 0
        if sum(nums[n-3:n]) == 3:
            return res
        return -1


nums = [0, 1, 1, 1, 0, 0]
output = 3

obj = Solution()
res = obj.minOperations(nums)
print(res)
print(output)
print(res == output)
