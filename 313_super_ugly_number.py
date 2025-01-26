import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        heap = [1]
        prev = 0
        moves = 0
        while moves < n:
            cur = heapq.heappop(heap)
            if cur == prev:
                continue
            for prime in primes:
                heapq.heappush(heap, cur * prime)
            prev = cur
            moves += 1
        return cur


n = 12
primes = [2, 7, 13, 19]
output = 32

obj = Solution()
res = obj.nthSuperUglyNumber(n, primes)
print(res)
print(output)
print(res == output)
