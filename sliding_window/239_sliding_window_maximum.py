from typing import List

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Output = [3, 3, 5, 5, 6, 7]

# nums = [1, -1]
# k = 1

# Expected = [1, -1]

# Create a sorted window that we use a binary search on to add and pop numbers to
# This requires some extra operations for popping and adding but lets use easily find the largest number to add to the result array.


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 1
        window = [nums[0]]
        while i < k:
            num = nums[i]
            l = 0
            r = len(window) - 1
            while l <= r:
                mid = (r - l) // 2
                print(mid)
                if num > window[mid]:
                    l = mid + 1
                elif num < window[mid]:
                    r = mid - 1
                else:
                    break
            if num < window[mid]:
                window.insert(mid, num)
            else:
                window.insert(mid+1, num)
            i += 1
        print(window)


obj = Solution()
result = obj.maxSlidingWindow(nums, k)
print(result)
