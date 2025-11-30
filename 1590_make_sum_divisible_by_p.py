class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        # we'll use up to prev (inclusive) if p-right is in prev
        prev = {0: -1}
        right = sum(nums)
        if right < p:
            return -1
        if not right % p:
            return 0

        res = n+1
        left = 0
        for i in range(n):
            rem = right % p
            if p-rem in prev:
                res = min(res, i-(prev[p-rem]+1))
            if not rem and right >= p:
                res = min(res, i-(prev[0]+1))
            left += nums[i]
            left %= p
            if not left:
                prev[0] = i
                left += p
            prev[left] = i
            right -= nums[i]

        if p in prev:
            res = min(res, n-(prev[p]+1))
        if res > n:
            return -1
        return res


nums = [6, 3, 5, 2]
p = 9
output = 2


obj = Solution()
res = obj.minSubarray(nums, p)
print(res)
print(output)
print(res == output)
