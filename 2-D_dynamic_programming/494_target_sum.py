class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        total = sum(nums)
        hmap = {0: 1}
        for i in range(len(nums)):
            temp = {}
            total -= nums[i]
            for key in hmap:
                for newKey in [key + nums[i], key - nums[i]]:
                    if abs(target - newKey) > total:
                        continue
                    if newKey in temp:
                        temp[newKey] += hmap[key]
                    else:
                        temp[newKey] = hmap[key]
            hmap = temp
        if target in hmap:
            return hmap[target]
        return 0


nums = [1, 1, 1, 1, 1]
target = 3
output = 5


obj = Solution()
res = obj.findTargetSumWays(nums, target)
print(res)
print(res == output)
