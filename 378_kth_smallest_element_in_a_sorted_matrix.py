import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix[0])

        heap = []
        for i, row in enumerate(matrix):
            heapq.heappush(heap, (row[0], i, 0))
        count = 1
        while count < k:
            cur = heapq.heappop(heap)
            val, row, col = cur
            if col < m-1:
                col+=1
                heapq.heappush(heap, (matrix[row][col], row, col))
            count += 1

        return heap[0][0]


matrix = [[1,2],[1,3]]
k = 2
output = 1


obj = Solution()
res = obj.kthSmallest(matrix, k)
print(res)
print(output)
print(res == output)