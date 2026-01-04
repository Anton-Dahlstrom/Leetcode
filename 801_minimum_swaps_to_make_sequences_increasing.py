class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        swapped = 1
        same = 0
        for i in range(1, n):
            bestSame = float("inf")
            bestSwap = float("inf")
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                bestSame = same
                bestSwap = min(bestSwap, swapped+1)
            if nums2[i] > nums1[i-1] and nums1[i] > nums2[i-1]:
                bestSame = min(bestSame, swapped)
                bestSwap = min(bestSwap, same+1)
            swapped = bestSwap
            same = bestSame

        return min(same, swapped)


nums1 = [1, 3, 5, 4]
nums2 = [1, 2, 3, 7]
output = 1

obj = Solution()
res = obj.minSwap(nums1, nums2)
print(res)
print(output)
print(res == output)
