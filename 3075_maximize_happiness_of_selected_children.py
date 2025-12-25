class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()
        res = 0
        for i in range(k):
            cur = happiness.pop() - i
            if cur <= 0:
                break
            res += cur

        return res


happiness = [1, 1, 1, 1]
k = 2
output = 1

obj = Solution()
res = obj.maximumHappinessSum(happiness, k)
print(res)
print(output)
print(res == output)
