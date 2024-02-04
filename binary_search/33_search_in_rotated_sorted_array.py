
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
Output: 4

# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3
# Output: -1

# nums = [1]
# target = 0
# Output: -1

# nums = [1, 3]
# target = 2
# Output: 0

nums = [1, 3]
target = 3
Output: 1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r-l) // 2
            print(l, r, mid)
            if nums[l] == target:
                return l
            if target in range(min(nums[mid], nums[r]), max(nums[mid], nums[r])):
                if nums[mid] > nums[r]:
                    r = mid - 1
                elif nums[mid] < nums[r]:
                    l = mid + 1
            elif target > max(nums[mid], nums[r]):
                if nums[r] > nums[mid]:
                    r = mid - 1
                elif nums[r] < nums[mid]:
                    l = mid + 1
            elif target < min(nums[mid], nums[r]):
                if nums[r] > nums[mid]:
                    r = mid - 1
                elif nums[r] < nums[mid]:
                    l = mid + 1

        return -1


obj = Solution()
answer = obj.search(nums, target)
print(answer)
