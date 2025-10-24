from typing import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            cnt = Counter(str(n))
            valid = True
            for key in cnt:
                if cnt[key] != int(key):
                    valid = False
                    break
            if valid:
                return n


n = 1000
output = 1333

obj = Solution()
res = obj.nextBeautifulNumber(n)
print(res)
print(output)
print(res == output)
