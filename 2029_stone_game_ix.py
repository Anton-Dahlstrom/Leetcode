from collections import defaultdict
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def simulate(cur, zero, one, two):
            iters = 1
            while zero or one or two:
                if cur == 2:
                    if two:
                        two -= 1
                        cur = 1
                    elif zero:
                        zero -= 1
                    else:
                        return iters
                elif cur == 1:
                    if one:
                        one -= 1
                        cur = 2
                    elif zero:
                        zero -= 1
                    else:
                        return iters
                iters += 1
            return iters

        n = len(stones)
        hmap = defaultdict(int)
        for i in range(n):
            hmap[stones[i] % 3] += 1
        if hmap[1]:
            iters = simulate(1, hmap[0], hmap[1]-1, hmap[2])
            if iters < n and iters % 2:
                return True
        if hmap[2]:
            iters = simulate(2, hmap[0], hmap[1], hmap[2]-1)
            print(iters)
            if iters < n and iters % 2:
                return True
        return False
