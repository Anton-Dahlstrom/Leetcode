from sortedcontainers import SortedList


class Solution:
    def minInversionCount(self, nums: list[int], k: int) -> int:
        sortedList = SortedList()
        n = len(nums)
        res = float("inf")
        inversions = 0
        for i in range(n):
            num = nums[i]
            if len(sortedList) == k:
                remove = nums[i-k]
                smaller = sortedList.bisect_left(remove)
                sortedList.remove(remove)
                inversions -= smaller

            bigger = len(sortedList) - sortedList.bisect_right(num)
            inversions += bigger
            sortedList.add(num)
            if len(sortedList) == k:
                res = min(res, inversions)
            if not res:
                return 0
        return res


nums = [5, 3, 2, 1]
k = 4
output = 6

obj = Solution()
res = obj.minInversionCount(nums, k)
print(res)
print(output)
print(res == output)
