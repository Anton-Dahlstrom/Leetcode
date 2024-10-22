class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        m -= 1
        n -= 1
        pointer = m + n + 1
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[pointer] = nums1[m]
                m -= 1
            else:
                nums1[pointer] = nums2[n]
                n -= 1
            pointer -= 1

        while n > -1:
            nums1[pointer] = nums2[n]
            n -= 1
            pointer -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
output = [1, 2, 2, 3, 5, 6]


obj = Solution()
res = obj.merge(nums1, m, nums2, n)
print(res)
print(output)
print(res == output)
