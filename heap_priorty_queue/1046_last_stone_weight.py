from typing import List
import heapq

stones = [2, 7, 4, 1, 8, 1]
Output: 1


class MaxHeap:
    def heapify(self, heap):
        for i in range(0, len(heap)):
            self.moveup(heap, i)

    def moveup(self, heap, child):
        parent = (child - 1)//2
        while child > 0 and heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = (child - 1)//2

    def movedown(self, heap, parent):
        child1 = parent * 2 + 1
        child2 = parent * 2 + 2
        while parent < len(heap) and child1 < len(heap) and (heap[parent] < heap[child1] or heap[parent] < heap[child2]):
            if heap[child1] > heap[child2]:
                child = child1
            else:
                child = child2
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child1 = parent * 2 + 1
            child2 = parent * 2 + 2

        if child2 < len(heap):
            if heap[parent] < heap[child2]:
                heap[parent], heap[child] = heap[child], heap[parent]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        heap.heapify(stones)


obj = Solution()
res = obj.lastStoneWeight(stones)
print(res)
