import heapq


class Solution:
    def findMaxVal(self, n: int, restrictions: list[list[int]], diff: list[int]) -> int:
        res = 0
        prefix = [0]*(n)
        cur = 0
        for i in range(n-1):
            cur += diff[i]
            prefix[i+1] = cur
        heap = []
        for i, maxval in restrictions:
            heapq.heappush(heap, (maxval+prefix[i], i, maxval))

        cur = 0
        diffUsed = 0
        for i in range(1, n):
            while heap and heap[0][1] < i:
                heapq.heappop(heap)
            if not heap:
                cur += diff[i-1]
            else:
                diffUsed += diff[i-1]
                maxval = heap[0][0] - diffUsed
                cur = min(cur+diff[i-1], maxval)
            res = max(cur, res)
        return res


n = 8
restrictions = [[3, 2]]
diff = [3, 5, 2, 4, 2, 3, 1]
output = 12


obj = Solution()
res = obj.findMaxVal(n, restrictions, diff)
print(res)
print(output)
print(res == output)
