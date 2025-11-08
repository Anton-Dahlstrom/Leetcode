class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            tarcnt = 0
            other = 0
            for j in range(i, n):
                val = nums[j]
                if val == target:
                    tarcnt += 1
                else:
                    other += 1
                if tarcnt > other:
                    res += 1

        return res


nums = [1, 2, 2, 3]
target = 2
output = 5

obj = Solution()
res = obj.countMajoritySubarrays(nums, target)
print(res)
print(output)
print(res == output)
