from collections import Counter, defaultdict
from typing import List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        unique = defaultdict(int)
        for key in cnt:
            val = cnt[key]
            unique[val] += 1
        for num in nums:
            if unique[cnt[num]] == 1:
                return num
        return -1
