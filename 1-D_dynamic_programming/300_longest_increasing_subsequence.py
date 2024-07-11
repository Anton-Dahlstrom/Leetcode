from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(arr, val):
            l = 0
            r = len(arr)-1
            while l <= r:
                mid = l + ((r-l)//2)
                if val == arr[mid]:
                    return mid
                if val < arr[mid]:
                    l = mid+1
                else:
                    r = mid-1
            if val < arr[mid]:
                mid += 1
            return mid

        arr = [nums[-1]]
        for val in nums[-2::-1]:
            if val < arr[-1]:
                arr.append(val)
                continue
            index = binarySearch(arr, val)
            arr[index] = val
        return len(arr)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
output = 4

nums = [4, 10, 4, 3, 8, 9]
output = 3

obj = Solution()
res = obj.lengthOfLIS(nums)
print(res)
print(res == output)
