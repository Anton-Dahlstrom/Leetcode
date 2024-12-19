
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hmap = {}
        for i, n in enumerate(nums):
            if n not in hmap:
                hmap[n] = i
            else:
                if abs(i - hmap[n]) <= k:
                    return True
                hmap[n] = i
        return False


nums = [1, 2, 3, 1]
k = 3
output = True

obj = Solution()
res = obj.containsNearbyDuplicate(nums, k)
print(res)
print(output)
print(res == output)
