from typing import List
import heapq

stones = [2, 7, 4, 1, 8, 1]
Output: 1


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        print(stones)


obj = Solution()
res = obj.lastStoneWeight(stones)
print(res)
