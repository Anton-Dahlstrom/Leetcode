import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        nums = (2, 3, 5)

        count = 0
        prev = -1
        while count < n:
            cur = heapq.heappop(heap)
            if cur == prev:
                continue
            for num in nums:
                heapq.heappush(heap, cur*num)
            prev = cur
            count += 1

        return cur


n = 10
output = 12


obj = Solution()
res = obj.nthUglyNumber(n)
print(res)
print(output)
print(res == output)
