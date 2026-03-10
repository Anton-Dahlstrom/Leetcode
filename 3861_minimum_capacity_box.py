class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n = len(capacity)
        smallest = float("inf")
        res = -1
        for i in range(n):
            if capacity[i] >= itemSize and capacity[i] < smallest:
                smallest = capacity[i]
                res = i
        return res
