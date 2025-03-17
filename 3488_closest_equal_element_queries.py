from collections import defaultdict


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        m = len(queries)
        indexes = [0] * n
        res = [-1] * m
        hmap = defaultdict(list)
        # Use value of a queried number to find it's subarray of indexes.
        # Each index in nums can also be used to find the index of the number
        # in its values array of indexes.
        # For example the third 4 we find gets index 2 stored in the
        # indexes array under the actual index of that specific 4 in nums.
        for i in range(n):
            val = nums[i]
            indexes[i] = len(hmap[val])
            hmap[val].append(i)
        for query in range(m):
            i = queries[query]
            val = nums[i]
            index = indexes[i]
            left = float("inf")
            right = float("inf")
            size = len(hmap[val])

            if hmap[val][index-1] != hmap[val][index]:
                big = max(hmap[val][index-1], hmap[val][index])
                small = min(hmap[val][index-1], hmap[val][index])
                left = min(big-small, abs((big-n)-small))

            if hmap[val][(index+1) % size] != hmap[val][index]:
                big = max(hmap[val][(index+1) % size], hmap[val][index])
                small = min(hmap[val][(index+1) % size], hmap[val][index])
                right = min(big-small, abs((big-n)-small))
            best = min(left, right)
            if best < float("inf"):
                res[query] = best
        return res


nums = [14, 14, 4, 2, 19, 19, 14, 19, 14]
queries = [2, 4, 8, 6, 3]
output = [-1, 1, 1, 2, -1]

obj = Solution()
res = obj.solveQueries(nums, queries)
print(res)
print(output)
print(res == output)
