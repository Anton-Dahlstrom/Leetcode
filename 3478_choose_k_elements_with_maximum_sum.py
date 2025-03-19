import heapq


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n = len(nums1)
        res = [0] * n
        nums1 = [(nums1[i], i) for i in range(n)]
        nums1.sort()
        # start from 0 and add numbers from nums2 as we go into a heapq
        # keep track of the sum of the heapq and when it's size exceeds k
        # we pop the smallest number and remove it from the sum
        cursum = 0
        heap = []
        prevadded = nums1[0][0]
        prevsum = 0
        for i in range(n):
            if nums1[i][0] != prevadded:
                prevsum = cursum
                prevadded = nums1[i][0]
            res[nums1[i][1]] = prevsum
            val = nums2[nums1[i][1]]
            cursum += val
            heapq.heappush(heap, val)
            if len(heap) > k:
                cursum -= heapq.heappop(heap)

        return res


nums1 = [4, 2, 1, 5, 3]
nums2 = [10, 20, 30, 40, 50]
k = 2
output = [80, 30, 0, 80, 50]

obj = Solution()
res = obj.findMaxSum(nums1, nums2, k)
print(res)
print(output)
print(res == output)
