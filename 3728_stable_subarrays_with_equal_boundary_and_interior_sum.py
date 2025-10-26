from collections import defaultdict


class Solution:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        prefix = [0]*n
        states = defaultdict(int)  # num, prefix
        res = 0
        for i in range(n):
            num = capacity[i]
            prefix[i] = prefix[i-1] + num
            needed = (num, prefix[i]-((prefix[i] - prefix[i-1])*2))
            res += states[needed]
            if i:
                states[(capacity[i-1], prefix[i-1])] += 1  # to avoid size 2
        return res


capacity = [-4, 4, 0, 0, -8, -4]
output = 1


obj = Solution()
res = obj.countStableSubarrays(capacity)
print(res)
print(output)
print(res == output)
