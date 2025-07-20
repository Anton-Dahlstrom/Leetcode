from collections import defaultdict


class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        count = defaultdict(int)
        arr = list(zip(values, labels))
        arr.sort(reverse=True)
        n = len(values)
        res = 0
        used = 0
        for i in range(n):
            label = arr[i][1]
            value = arr[i][0]
            if count[label] >= useLimit:
                continue
            count[label] += 1
            res += value
            used += 1
            if used >= numWanted:
                break
        return res


values = [5, 4, 3, 2, 1]
labels = [1, 1, 2, 2, 3]
numWanted = 3
useLimit = 1
output = 9

values = [2, 6, 1, 2, 6]
labels = [2, 2, 2, 1, 1]
numWanted = 1
useLimit = 1
output = 6

obj = Solution()
res = obj.largestValsFromLabels(values, labels, numWanted, useLimit)
print(res)
print(output)
print(res == output)
