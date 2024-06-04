from typing import List

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Output = [3, 3, 5, 5, 6, 7]

nums = [1, -1]
k = 1
Output = [1, -1]


class Solution:
    def insertBinarySearch(self, num: int, window: list):
        if not window:
            window.append(num)
            return
        l = 0
        r = len(window) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if num == window[mid]:
                window.insert(mid, num)
                return
            elif num > window[mid]:
                l = mid + 1
            elif num < window[mid]:
                r = mid - 1
        if num < window[mid]:
            window.insert(mid, num)
        else:
            window.insert(mid+1, num)

    def removeBinarySearch(self, num: int, window: list):
        l = 0
        r = len(window) - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if num == window[mid]:
                window.pop(mid)
                return
            elif num < window[mid]:
                r = mid-1
            else:
                l = mid + 1

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(0, k):
            self.insertBinarySearch(nums[i], window)
        l = 0
        r = k
        res = [window[-1]]
        while r < len(nums):
            self.removeBinarySearch(nums[l], window)
            self.insertBinarySearch(nums[r], window)
            res.append(window[-1])
            l += 1
            r += 1
        return res


obj = Solution()
result = obj.maxSlidingWindow(nums, k)
print(result)
