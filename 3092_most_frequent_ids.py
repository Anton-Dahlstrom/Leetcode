from collections import defaultdict
import heapq


class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        hmap = defaultdict(int)
        n = len(nums)
        heap = []
        res = [0]*n
        for i in range(n):
            hmap[nums[i]] += freq[i]
            heapq.heappush(heap, (hmap[nums[i]]*-1, nums[i]))
            while heap[0][0] != hmap[heap[0][1]]*-1:
                heapq.heappop(heap)
            res[i] = (heap[0][0]*-1)
        return res


nums = [2, 3, 2, 1]
freq = [3, 2, -3, 1]
output = [3, 3, 2, 2]

obj = Solution()
res = obj.mostFrequentIDs(nums, freq)
print(res)
print(output)
print(res == output)
