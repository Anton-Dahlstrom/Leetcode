class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        hmap = {}
        res = float("inf")
        for i, num in enumerate(nums):
            if num in hmap:
                res = min(res, abs(i-hmap[num]))
            rev = int(str(num)[::-1])
            hmap[rev] = i
        if res == float("inf"):
            return -1
        return res


nums = [12, 21, 45, 33, 54]
output = 1

obj = Solution()
res = obj.minMirrorPairDistance(nums)
print(res)
print(output)
print(res == output)
