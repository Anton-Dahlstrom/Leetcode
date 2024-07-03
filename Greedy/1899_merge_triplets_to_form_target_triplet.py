from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i, val in enumerate(target):
            triplets = [triplet for triplet in triplets if triplet[i] <= val]
        best = [max(val) for val in zip(*triplets)]
        if best == target:
            return True
        return False


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
output = True

obj = Solution()
res = obj.mergeTriplets(triplets, target)
print(res)
print(res == output)
