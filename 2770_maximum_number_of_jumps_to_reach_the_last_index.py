class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        paths = [0]*n
        for i in range(n):
            if i and not paths[i]:
                continue
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) <= target:
                    paths[j] = max(paths[i] + 1, paths[j])
        return paths[-1] if paths[-1] else -1


nums = [0, 2, 1, 3]
target = 1
output = -1

obj = Solution()
res = obj.maximumJumps(nums, target)
print(res)
print(output)
print(res == output)
