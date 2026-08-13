from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, sum(quantities)
        while l <= r:
            mid = l + ((r-l)//2)
            if self.fits(mid, quantities, n):
                r = mid-1
            else:
                l = mid+1
        return l

    def fits(self, target, arr, stores) -> bool:
        for i in range(len(arr)):
            stores -= arr[i] // target
            if arr[i] % target:
                stores -= 1
        return stores >= 0
