class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n:
            j = max(i+1, j)
            while j < m and nums2[j] >= nums1[i]:
                j += 1
            res = max(j-i-1, res)
            i += 1
        return res


nums1 = [55, 30, 5, 4, 2]
nums2 = [100, 20, 10, 10, 5]
output = 2

obj = Solution()
res = obj.maxDistance(nums1, nums2)
print(res)
print(output)
print(res == output)
