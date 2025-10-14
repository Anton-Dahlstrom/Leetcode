class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        stops = [0]
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                stops.append(i)
        if len(stops) == 1 and len(nums) >= k*2:
            return True
        stops.append(n)
        for i in range(1, len(stops)-1):
            if stops[i] - stops[i-1] >= k*2 or stops[i+1] - stops[i] >= k*2 or (stops[i] - stops[i-1] >= k and stops[i+1] - stops[i] >= k):
                return True
        return False


nums = [8, -4, -1, 16, 20]
k = 2
output = True

obj = Solution()
res = obj.hasIncreasingSubarrays(nums, k)
print(res)
print(output)
print(res == output)
