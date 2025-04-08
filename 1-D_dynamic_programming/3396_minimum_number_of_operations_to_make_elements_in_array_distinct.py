class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        hset = set()
        i = n-1
        while i >= 0:
            if nums[i] in hset:
                break
            hset.add(nums[i])
            i -= 1
        res = (i+1)//3
        if (i+1) % 3:
            res += 1
        return res


nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
output = 2


obj = Solution()
res = obj.minimumOperations(nums)
print(res)
print(output)
print(res == output)
