from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        l, r = 0, 0
        n = len(s)
        res = 0
        while r < n:
            char = s[r]
            hmap[char] += 1
            while hmap[char] > 2:
                hmap[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r-l)
        return res
