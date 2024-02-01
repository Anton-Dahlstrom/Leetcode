nums = [3, 4, 5, 1, 2]
Output: 1

nums = [11, 13, 15, 17]
Output: 11

nums = [1]
Output: 0

nums = [2, 3, 1]
Output: 1


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            # if nums[l] < nums[mid] and nums[l] < nums[r]:
            #     return nums[l]
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
        # if mid:
        return nums[mid]
        print("hi")
        return min(nums)


obj = Solution()
answer = obj.findMin(nums)
print(answer)
