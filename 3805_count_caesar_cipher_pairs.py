from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        n = len(words)
        m = len(words[0])
        hmap = defaultdict(int)
        res = 0
        for i in range(n):
            base = ord(words[i][0]) - 97
            hash = []
            for j in range(m):
                cur = ord(words[i][j]) - 97
                cur -= base
                if cur < 0:
                    cur += 26
                hash.append(str(cur))
            hash = ",".join(hash)
            res += hmap[hash]
            hmap[hash] += 1
        return res
