class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] == key:
                if not res or res[-1] < i+k:
                    if not res:
                        start = max(0, i-k)
                    else:
                        start = max(0, res[-1]+1, i-k)
                    res += [i for i in range(start, min(n, i+k+1))]
        return res


nums = [2, 1, 1, 1, 2]
key = 2
k = 1
output = [0, 1, 3, 4]

obj = Solution()
res = obj.findKDistantIndices(nums, key, k)
print(res)
print(output)
print(res == output)
