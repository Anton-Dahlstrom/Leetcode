from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        found = {}
        starts = []
        for i, char in enumerate(s):
            if char not in found:
                found[char] = i
                starts.append(i)
            else:
                while starts[-1] > found[char]:
                    starts.pop()
        starts.append(len(s))
        for i in reversed(range(1, len(starts))):
            starts[i] = starts[i] - starts[i-1]
        return starts[1:]


s = "ababcbacadefegdehijhklij"
output = [9, 7, 8]
obj = Solution()
res = obj.partitionLabels(s)
print(res)
print(res == output)
