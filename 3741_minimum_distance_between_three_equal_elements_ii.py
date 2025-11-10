from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        hmap = defaultdict(list)
        res = float("inf")
        for i, num in enumerate(nums):
            if len(hmap[num]) == 2:
                x = i-hmap[num][0]
                x += i-hmap[num][1]
                x += hmap[num][1] - hmap[num][0]
                res = min(res, x)
                hmap[num][0] = hmap[num][1]
                hmap[num][1] = i
            else:
                hmap[num].append(i)

        if res == float("inf"):
            res = -1
        return res


nums = [1, 2, 1, 1, 3]
output = 6

obj = Solution()
res = obj.minimumDistance(nums)
print(res)
print(output)
print(res == output)
