class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        pre, suf = 0, sum(nums)
        res = 0
        for num in nums[:-1]:
            pre += num
            suf += num
            if not (pre+suf) % 2:
                res += 1
        return res


nums = [10, 10, 3, 7, 6]
output = 4

obj = Solution()
res = obj.countPartitions(nums)
print(res)
print(output)
print(res == output)
