import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        queries.sort()
        n = len(nums)
        m = len(queries)
        j = 0
        activeEnds = []
        inactiveEnds = []
        res = 0
        for i in range(n):
            while activeEnds and activeEnds[0] < i:
                heapq.heappop(activeEnds)

            while inactiveEnds and (inactiveEnds[0]*-1) < i:
                heapq.heappop(inactiveEnds)
                res += 1

            # keep track of biggest end we can move to active
            while j < m and queries[j][0] <= i:
                heapq.heappush(inactiveEnds, queries[j][1] * -1)
                j += 1

            while nums[i] > len(activeEnds) and inactiveEnds:
                if (inactiveEnds[0] * -1) < i:
                    return -1
                heapq.heappush(
                    activeEnds, (heapq.heappop(inactiveEnds)*-1))
            if nums[i] > len(activeEnds):
                return -1

        return res + len(inactiveEnds)


nums = [1, 1, 1, 1]
queries = [[1, 3], [0, 2], [1, 3], [1, 2]]
output = 2


obj = Solution()
res = obj.maxRemoval(nums, queries)
print(res)
print(output)
print(res == output)
