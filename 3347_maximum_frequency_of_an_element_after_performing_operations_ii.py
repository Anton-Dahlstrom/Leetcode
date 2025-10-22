class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()
        size = min(10**9+2, nums[-1]+k+2)
        i = 0
        arr = []
        while i < n:
            val = 1
            while i < n-1 and nums[i] == nums[i+1]:
                val += 1
                i += 1
            l = max(0, nums[i]-k)
            r = min(size-1, nums[i]+k+1)
            arr.append((l, 0, val))  # index, flag, val
            arr.append((nums[i], 1, val))
            arr.append((r, 0, -val))
            i += 1
        arr.sort()
        res = 1
        cur = 0
        for i in range(len(arr)):
            if arr[i][1] == 1:
                res = max(res, min(numOperations + arr[i][2], cur))
            else:
                cur += arr[i][2]
                res = max(res, min(numOperations, cur))
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
