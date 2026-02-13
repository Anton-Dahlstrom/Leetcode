from collections import defaultdict
from pyparsing import List
import heapq


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        maxval = []
        minval = []
        hmax = defaultdict(int)
        hmin = defaultdict(int)
        l = 0
        for r in range(n):
            num = nums[r]
            heapq.heappush(minval, num)
            heapq.heappush(maxval, -num)
            while (l < r):
                if (-maxval[0] - minval[0]) * (r-l+1) <= k:
                    break
                hmax[-nums[l]] += 1
                hmin[nums[l]] += 1
                l += 1
                while maxval and hmax[maxval[0]] > 0:
                    hmax[maxval[0]] -= 1
                    heapq.heappop(maxval)
                while minval and hmin[minval[0]] > 0:
                    hmin[minval[0]] -= 1
                    heapq.heappop(minval)
            res += r-l+1
        return res
