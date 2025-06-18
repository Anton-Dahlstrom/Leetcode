class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            if nums[i+2] - nums[i] > k:
                return []
            res.append(nums[i:i+3])
        return res


nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2

output = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

obj = Solution()
res = obj.divideArray(nums, k)
print(res)
print(output)
print(res == output)
