class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        l = 0
        r = len(nums)-1
        mid = l + ((r-l)//2)

        if nums[mid] == target:
            return True
        if nums[l] == nums[mid]:
            if self.search(nums[l:mid], target):
                return True
            if self.search(nums[mid+1:r+1], target):
                return True
            return False

        while l <= r:
            mid = l + ((r-l)//2)
            if target == nums[mid]:
                return True
            if nums[l] > nums[mid]:  # biggest value is always after the larger number
                if target >= nums[l] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
output = True


obj = Solution()
res = obj.search(nums, target)
print(res)
print(output)
print(res == output)
