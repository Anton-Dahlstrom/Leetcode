import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [[nums[i], i] for i in range(len(nums))]
        heapq.heapify(heap)
        for _ in range(k):
            cur = heapq.heappop(heap)
            cur[0] *= multiplier
            nums[cur[1]] = cur[0]
            heapq.heappush(heap, cur)
        return nums


nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
output = [8, 4, 6, 5, 6]

obj = Solution()
res = obj.getFinalState(nums, k, multiplier)
print(res)
print(output)
print(res == output)
