class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if nums[mid] < target:
            return mid + 1
        return mid


nums = [1, 3, 6, 8]
target = 0
output = 0

obj = Solution()
res = obj.searchInsert(nums, target)
print(res)
print(output)
print(res == output)
