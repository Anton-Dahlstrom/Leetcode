from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            res += abs(arr[i] - brr[i])
        arr.sort()
        brr.sort()
        for i in range(n):
            k += abs(arr[i] - brr[i])
        return min(res, k)
