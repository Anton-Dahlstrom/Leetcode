from typing import Counter


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        cnt = Counter(deck)
        cnt = [cnt[key] for key in cnt]
        cnt.sort()
        divisible = [i for i in range(2, cnt[0]+1) if not cnt[0] % i]
        for count in cnt[1:]:
            divisible = [div for div in divisible if not count % div]
            if not divisible:
                return False
        if divisible:
            return True
        return False


deck = [1, 2, 3, 4, 4, 3, 2, 1]
output = True


obj = Solution()
res = obj.hasGroupsSizeX(deck)
print(res)
print(output)
print(res == output)
