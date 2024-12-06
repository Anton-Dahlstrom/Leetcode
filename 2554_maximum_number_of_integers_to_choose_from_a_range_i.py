class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        cursum = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            cursum += i
            if cursum > maxSum:
                break
            count += 1

        return count


banned = [1, 6, 5]
n = 5
maxSum = 6
output = 2

obj = Solution()
res = obj.maxCount(banned, n, maxSum)
print(res)
print(output)
print(res == output)
