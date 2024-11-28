class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) -1
        while True:
            mid = r-((r-l)//2)
            if mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                l = mid + 1
            elif mid > 0 and nums[mid-1] > nums[mid]:
                r = mid -1
            else:
                return mid


nums = [1,2,1,4,6,2,3,8,2,1]
output = [1, 5]

nums = [2,1]
output = 0

obj = Solution()
res = obj.findPeakElement(nums)
print(output)
print(res)
print(res == output)