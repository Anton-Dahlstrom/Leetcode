class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        res = 1
        dist = float("inf")
        end = nums2[-1]
        for i in range(n):
            small = min(nums1[i], nums2[i])
            big = max(nums1[i], nums2[i])
            if end in range(small, big+1):
                dist = 0
            if dist:
                dist = min(dist, abs(small-end), abs(big-end))
            res += abs(nums1[i] - nums2[i])
        return res + dist


nums1 = [458, 915]
nums2 = [709, 596, 318]
output = 711

obj = Solution()
res = obj.minOperations(nums1, nums2)
print(res)
print(output)
print(res == output)
