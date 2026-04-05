from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)
        res = []
        for key in cnt:
            if cnt[key] > n//3:
                res.append(key)
        return res
