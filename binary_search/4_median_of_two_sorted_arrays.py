from typing import List
# Split both arrays and remove everything below the smallest middle value and
# everything above the largest middle value. Note that this can't include the
# middle value.

# med = 6.5
# nums = [2, 4, 6, 8, 10, 12]
# nums2 = [1, 3, 5, 7, 9, 11]

nums = [1, 4, 5]
nums2 = [2, 3, 6, 7, 8]

# 0,3
# [1, 4, 5]
# [2, 3]
# 2,3
# [1, 4, 5]
# []
# 3,3
# [4, 5]

nums = [3]*5 + [4]*2
nums2 = [1]*5 + [9]*2
print(nums+nums2)
# quit()
# nums2 = [2, 3, 6, 7, 8]


# comb = [1,2,3,4,5,6,7,8]

# [2, 4, 5, 6, 7, ,9 ,11]
# botremoved = 2
# topremoved = 3
#  [2, 4, 6]
#  [5, 7, 9, 11]

#  [2, 4, 6]
#  [7, 9, 11]

# [4, 6]
# [7, 9]

# [6]
# [5]


# How can I ensure there are an equal amount of larger and smaller numbers removed?
# First we need to find out where less values got removed
# Then we move an extra from the opposite side that still maintains parity in the array sizes.
# This removal will also make it possible for the minvalue in one array to be larger than
# the maxvalue in the other, effectively giving us one sorted array and solving the problem.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findSortedList(nums1, nums2):
            def cutArrays(nums1, nums2):
                len1, len2 = len(nums1), len(nums2)
                diff = abs(len1 - len2)
                if not diff:
                    return
                elif len1 > len2:
                    pass

            def binarySearch(l, r, array):
                mid = l + ((r-l)//2)
                return (mid, array[mid])

            l1 = 0
            r1 = len(nums1) - 1
            l2 = 0
            r2 = len(nums2) - 1
            removedTop = 0
            removedBot = 0
            while True:
                print(nums1[l1:r1+1])
                print(nums2[l2:r2+1])
                # print(l1, r1, l2, r2)
                # print(removedTop, removedBot)
                mid1, val1 = binarySearch(l1, r1, nums1)
                mid2, val2 = binarySearch(l2, r2, nums2)

                if nums1[l1] > nums2[r2]:
                    return nums2[l2:r2+1] + nums1[l1:r1+1]
                elif nums2[l2] > nums1[r1]:
                    return nums1[l1:r1+1] + nums2[l2:r2+1]

                if mid1 in (l1, r1) or mid2 in (l2, r2):
                    arr = nums1[l1:r1+1] + nums2[l2:r2+1]
                    arr.sort()
                    return arr

                if val1 > val2:
                    removedTop += r1 - mid1
                    removedBot += mid2 - l2
                    r1 = mid1
                    l2 = mid2
                else:
                    removedTop += r2 - mid2
                    removedBot += mid1 - l1
                    l1 = mid1
                    r2 = mid2

                # Because of floor division we can only remove more large values.
                if removedTop != removedBot:
                    removedBot += 1
                    if val1 > val2:
                        l2 += 1
                        if nums1[l1] > nums2[r2]:
                            return nums2[l2:r2+1] + nums1[l1:r1+1]
                    else:
                        l1 += 1
                        if nums2[l2] > nums1[r1]:
                            return nums1[l1:r1+1] + nums2[l2:r2+1]

        if nums1 and nums2:
            res = findSortedList(nums1, nums2)
        else:
            res = nums1+nums2
        rlen = len(res)

        print(res)
        if rlen % 2:
            return res[rlen//2]
        return (res[rlen//2] + res[rlen//2-1])/2


obj = Solution()
res = obj.findMedianSortedArrays(nums, nums2)
print(res)