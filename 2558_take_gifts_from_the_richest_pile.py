import heapq
import math
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = [] 
        for gift in gifts:
            heapq.heappush(heap, gift*-1)
        for _ in range(k):
            val = heapq.heappop(heap)
            val = int(math.sqrt(val*-1))
            heapq.heappush(heap, val*-1)
        res = sum(heap) *-1
        return res

gifts = [25,64,9,4,100]
k = 4
output= 29

obj = Solution()
res = obj.pickGifts(gifts, k)
print(res)
print(output)
print(res == output)