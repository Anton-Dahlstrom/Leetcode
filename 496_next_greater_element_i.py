class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums2)
        m = len(nums1)
        indexes = {}
        res = [-1] * m
        for i in range(n):
            indexes[nums2[i]] = i
        for i in range(m):
            val = nums1[i]
            for j in range(indexes[val]+1, n):
                if nums2[j] > val:
                    res[i] = nums2[j]
                    break
        return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
output = [-1, 3, -1]

obj = Solution()
res = obj.nextGreaterElement(nums1, nums2)
print(res)
print(output)
print(res == output)
