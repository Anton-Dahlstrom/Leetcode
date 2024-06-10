from typing import List
# Split both arrays and remove everything below the smallest middle value and
# everything above the largest middle value. Note that this can't include the
# middle value.

# med = 6.5
nums = [2, 4, 6, 8, 10, 12]
nums2 = [1, 3, 5, 7, 9, 11]

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
        def binarySearch(l, r, array):
            mid = l + ((r-l)//2)
            return (mid, array[mid])
        l1 = 0
        r1 = len(nums1) - 1
        l2 = 0
        r2 = len(nums2) - 1
        len1 = len(nums1)
        len2 = len(nums2)
        removedTop = 0
        removedBot = 0
        # removedTop = (len1 - r1-1) + (len2 - r2-1)
        # removedBot = l1 + l2
        while True:
            mid1, val1 = binarySearch(l1, r1, nums1)
            mid2, val2 = binarySearch(l2, r2, nums2)
            if nums1[l1] > nums2[r2] or nums2[l2] > nums1[r1]:
                break
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
                if val1 > val2:
                    if nums1[l1] > nums2[r2]:
                        # Need to implement logic for how to deal with sorted arrays
                        # and when the arrays become small because we're assigning r/l to mid instead
                        # of shifting it by 1 like you do in regular binary search.
                        break
                    else:
                        l2 += 1
                else:
                    if nums2[l2] > nums1[r1]:
                        break
                    else:
                        l1 += 1

            print("removed:", removedTop, removedBot)
            print(l1, r1, l2, r2)
            print(mid1, mid2)
            break


obj = Solution()
res = obj.findMedianSortedArrays(nums, nums2)
print(res)
