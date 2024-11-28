class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        def findMax(nums):
            l = 0
            r = len(nums)

            while l <= r:
                mid = r - ((r-l)//2)
                print(l, mid, r)
                if nums[l] > nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            print(l, mid, r)
            if nums[l] > nums[mid]:
                return l

            return mid

        maxindex = findMax(nums)
        print(maxindex)

nums = [2,5,6,0,0,1,2]
target = 3
output = False

obj = Solution()
res = obj.search(nums, target)
print(res)
print(output)
print(res == output)