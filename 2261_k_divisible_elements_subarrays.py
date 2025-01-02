class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        perms = set()
        for l in range(len(nums)):
            count = 0
            if not nums[l] % p:
                count += 1
            perms.add(nums[l])
            for r in range(l+1, len(nums)):
                if not nums[r] % p:
                    count += 1
                if count > k:
                    break
                perms.add(tuple(nums[l:r+1]))
        return len(perms)


nums = [2, 3, 3, 2, 2]
k = 2
p = 2
output = 11

obj = Solution()
res = obj.countDistinct(nums, k, p)
print(res)
print(output)
print(res == output)
