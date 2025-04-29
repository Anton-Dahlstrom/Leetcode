class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maxnum = max(nums)
        n = len(nums)
        cnt = 0
        res = 0
        r = 0
        for l in range(n):
            while r < n and cnt < k:
                if nums[r] == maxnum:
                    cnt += 1
                r += 1
            if cnt < k:
                break
            res += n-r+1
            if nums[l] == maxnum:
                cnt -= 1
        return res


nums = [1, 3, 2, 3, 3]
k = 2
output = 6


obj = Solution()
res = obj.countSubarrays(nums, k)
print(res)
print(output)
print(res == output)
