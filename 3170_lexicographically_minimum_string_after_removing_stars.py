
import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        heap = []
        remove = set()
        for i in range(n):
            if s[i] == "*":
                remove.add(heapq.heappop(heap)[1])
            else:
                heapq.heappush(heap, (ord(s[i]), i * -1))
        res = ""
        for i in range(n):
            if s[i] != "*" and i*-1 not in remove:
                res += s[i]
        return res


s = "aaba*"
output = "aab"

obj = Solution()
res = obj.clearStars(s)
print(res)
print(output)
print(res == output)
