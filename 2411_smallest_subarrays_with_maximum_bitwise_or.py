from collections import defaultdict


class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * n
        cur = 0
        for i in range(n-1, -1, -1):
            cur |= nums[i]
            size = bin(cur).count("1")
            prefix[i] = size

        count = defaultdict(int)
        res = [0]*n
        l, r = 0, 0
        while l < n:
            while r <= l or len(count) < prefix[l]:
                for i, bit in enumerate(bin(nums[r])[-1:1:-1]):
                    if bit == "1":
                        count[i] += 1
                r += 1
            res[l] = r-l
            for i, bit in enumerate(bin(nums[l])[-1:1:-1]):
                if bit == "1":
                    count[i] -= 1
                    if not count[i]:
                        count.pop(i)
            l += 1
        return res


nums = [1, 0, 2, 1, 3]
output = [3, 3, 2, 2, 1]


obj = Solution()
res = obj.smallestSubarrays(nums)
print(res)
print(output)
print(res == output)
