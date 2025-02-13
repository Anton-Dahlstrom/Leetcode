import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            count += 1
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            new = (min(n1, n2) * 2) + max(n1, n2)
            heapq.heappush(nums, new)
        return count


nums = [1, 1, 2, 4, 9]
k = 20
output = 4

obj = Solution()
res = obj.minOperations(nums, k)
print(res)
print(output)
print(res == output)
