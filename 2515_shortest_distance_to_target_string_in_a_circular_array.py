from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = float("inf")
        for i in range(n):
            if words[i] == target:
                if i <= startIndex:
                    res = min(res, startIndex-i)
                    res = min(res, i + n-startIndex)
                else:
                    res = min(res, i-startIndex)
                    res = min(res, startIndex + n - i)
        if res == float("inf"):
            return -1
        return res
