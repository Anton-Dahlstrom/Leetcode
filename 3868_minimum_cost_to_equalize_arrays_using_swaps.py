from collections import defaultdict
from typing import Counter


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        cnt = Counter(nums1)
        temp = defaultdict(int)
        for i in range(n):
            cur = nums2[i]
            if cur in cnt and cnt[cur] > 0:
                cnt[cur] -= 1
            else:
                temp[cur] += 1
        if not temp:
            return 0

        for key in cnt:
            if cnt[key] > 0:
                temp[key] += cnt[key]
        res = 0
        for key in temp:
            if temp[key] % 2:
                return -1
            res += temp[key]

        return res//4


nums1 = [10, 20]
nums2 = [20, 10]
output = 0

obj = Solution()
res = obj.minCost(nums1, nums2)
print(res)
print(output)
print(res == output)
