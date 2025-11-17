class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        dist = len(nums)
        for num in nums:
            if num == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
        return True


nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2
output = True

obj = Solution()
res = obj.kLengthApart(nums, k)
print(res)
print(output)
print(res == output)
