class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def bruteForce(cap):
            i = 0
            robbed = 0
            while i < len(nums):
                if nums[i] <= cap:
                    robbed += 1
                    i += 2
                    if robbed == k:
                        return True
                else:
                    i += 1
            return False

        if len(nums) > 50:
            r = max(nums)
        else:
            r = 10**9
        l = 0

        while l < r:
            mid = l + ((r-l)//2)
            if bruteForce(mid):
                r = mid
            else:
                l = mid+1
        return l


nums = [2, 3, 5, 9]
k = 2
output = 5

obj = Solution()
res = obj.minCapability(nums, k)
print(res)
print(output)
print(res == output)
