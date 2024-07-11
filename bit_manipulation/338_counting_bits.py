from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        while n > 0:
            count = 0
            start = n
            while start:
                temp = start
                temp >>= 1
                temp <<= 1
                if start != temp:
                    count += 1
                start >>= 1
            arr[n] = count
            n -= 1
        return arr


n = 5
output = [0, 1, 1, 2, 1, 2]

obj = Solution()
res = obj.countBits(n)
print(res)
print(res == output)
