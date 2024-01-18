# nums = [-1,0,3,5,9,12]
# target = 9
# 4

# nums = [-1,0,3,5,9,12]
# target = 2
# -1

nums = [5]
target = 5
0

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] == target:
            return l
        while r > l:
            distance = (r - l) // 2
            if not distance:
                distance = 1
            index = l + distance
            if nums[index] == target:
                return index
            if nums[index] > target:
                r = r - distance
            else:
                l = l + distance
        return - 1

obj = Solution()
answer = obj.search(nums, target)
print(answer)