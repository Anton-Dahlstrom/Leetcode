from typing import List
nums = [1, 4, 5, 9]
nums2 = [2, 3, 6, 7, 8]
# [1,2,3,4,5,6,7,8,9]
# 0, 4
# candidates = [1,2,3,4,5]
# [1,4,5]
# [2,3]

# Find middle index and value of the larger array.
# Move the index and reassign value based on how many smaller/larger values
# exist in the small array.

# It finds the value 6 in the large array.
# All the numbers are smaller which means


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        if len1 > len2:
            if len1 % 2:
                mid = nums1[len1//2]
            else:
                mid = nums1[len1//2-1: len1//2+1]

        elif len1 < len2:
            if len2 % 2:
                mid = nums2[len2//2]
            else:
                mid = nums2[len2//2-1: len2//2+1]
        print(mid)


obj = Solution()
res = obj.findMedianSortedArrays(nums, nums2)
print(res)
