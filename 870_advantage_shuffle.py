class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        nums2 = [(nums2[i], i) for i in range(n)]
        nums2.sort()
        nums1.sort()
        res = [0]*n
        l, r = 0, n-1
        for i in range(n-1, -1, -1):
            val, index = nums2[i]
            if nums1[r] > val:
                res[index] = nums1[r]
                r -= 1
            else:
                res[index] = nums1[l]
                l += 1
        return res


nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]
output = [2, 11, 7, 15]

obj = Solution()
res = obj.advantageCount(nums1, nums2)
print(res)
print(output)
print(res == output)
