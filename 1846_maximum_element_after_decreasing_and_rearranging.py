from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        res = 0
        for i in range(n):
            if arr[i] > res:
                res += 1
        return res
