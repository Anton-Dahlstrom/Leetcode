class Solution:
    def countElements(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if not k:
            return n
        nums.sort()
        cap = nums[-k]
        i = n-k-1
        while i >= 0:
            if nums[i] < cap:
                return i+1
            i -= 1
        return 0


nums = [3, 1, 2]
k = 1
output = 2

obj = Solution()
res = obj.countElements(nums, k)
print(res)
print(output)
print(res == output)
