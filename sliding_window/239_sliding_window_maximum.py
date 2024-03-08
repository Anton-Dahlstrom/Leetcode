from typing import List

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Output = [3, 3, 5, 5, 6, 7]

nums = [1, -1]
k = 1

Expected = [1, -1]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        largest = max(nums[l:r+1])
        result = [largest]
        l += 1
        r += 1
        while r < len(nums):
            if nums[r] > largest:
                largest = nums[r]
            elif nums[l-1] >= largest:
                largest = max(nums[l:r+1])
            result.append(largest)
            r += 1
            l += 1
        return result


obj = Solution()
result = obj.maxSlidingWindow(nums, k)
print(result)
