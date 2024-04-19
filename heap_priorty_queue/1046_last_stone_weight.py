from typing import List
import heapq

stones = [2, 7, 4, 1, 8, 1]
Output: 1


class MinHeap:
    def heapify(self, heap):
        for i in range(0, len(heap)):
            self.moveup(heap, i)

    def moveup(self, heap, child):
        parent = (child - 1)//2
        while child > 0 and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = (child - 1)//2


minheap = MinHeap()
minheap.heapify(stones)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        print(stones)


obj = Solution()
res = obj.lastStoneWeight(stones)
print(res)
