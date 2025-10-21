from collections import Counter


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        n = len(nums)
        cnt = Counter(nums)
        nums.sort()
        size = min(10**5+2, nums[-1]+k+2)
        arr = [0]*size
        for i in range(n):
            l = max(0, nums[i]-k)
            r = min(size-1, nums[i]+k+1)
            arr[l] += 1
            arr[r] -= 1
        res = 1
        cur = 0
        for i in range(size):
            cur += arr[i]
            res = max(res, min(numOperations+cnt[i], cur))
        return res


nums = [1, 2, 4, 5]
k = 2
numOperations = 4
output = 4


obj = Solution()
res = obj.maxFrequency(nums, k, numOperations)
print(res)
print(output)
print(res == output)
