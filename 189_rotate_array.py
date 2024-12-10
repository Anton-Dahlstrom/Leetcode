class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]


nums =[1, 2, 3, 4, 5, 6, 7]
k = 3
output = [5, 6, 7, 1, 2, 3, 4] 


obj = Solution()
res = obj.rotate(nums, k)
print(nums)
print(output)
print(nums == output)