from typing import List
import heapq

stones = [2, 7, 4, 1, 8, 1]
Output: 1
stones = [2, 2]
Output: 0
stones = [434, 667, 378, 919, 212, 902, 240, 257, 208, 996, 411, 222, 557, 634,
          425, 949, 755, 833, 785, 886, 40, 159, 932, 157, 764, 916, 85, 300, 130, 278]
Output: 1

stones = [328, 677, 517, 654, 931, 961, 511, 408, 932, 36, 618, 450, 919, 235,
          931, 933, 60, 413, 248, 942, 978, 827, 115, 32, 306, 493, 944, 754, 385, 145]
Output: 1


class MaxHeap:
    def heapify(self, heap):
        for i in range(0, len(heap)):
            self.moveup(heap, i)

    def moveup(self, heap, child):
        parent = (child - 1)//2
        while child < len(heap) and parent >= 0 and heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = (child - 1)//2

    def movedown(self, heap, parent):
        child1 = parent * 2 + 1
        child2 = parent * 2 + 2

        while (child1 < len(heap) and heap[child1] > heap[parent]) or (child2 < len(heap) and heap[child2] > heap[parent]):
            if child2 < len(heap) and heap[child2] > heap[child1]:
                child = child2
            else:
                child = child1
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child1 = parent * 2 + 1
            child2 = parent * 2 + 2
        return parent

    def remove(self, heap, index):
        heap[index], heap[-1] = heap[-1], heap[index]
        heap.pop()
        self.movedown(heap, index)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        heap.heapify(stones)
        while len(stones) > 1:
            if len(stones) == 2:
                child = 1
            elif stones[1] > stones[2]:
                child = 1
            else:
                child = 2
            stones[0] = stones[0] - stones[child]
            heap.remove(stones, child)
            if not stones[0]:
                heap.remove(stones, 0)
            else:
                heap.movedown(stones, 0)
        if not stones:
            return 0
        return stones[0]


obj = Solution()
res = obj.lastStoneWeight(stones)
print(res)
