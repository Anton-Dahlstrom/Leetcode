from collections import defaultdict


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        cnt = defaultdict(int)
        res = []
        for i in range(n):
            cnt[nums[i]] += 1
            if i >= k-1:
                arr = sorted([(cnt[k], k) for k in cnt], reverse=True)
                temp = 0
                for j in range(min(x, len(arr))):
                    temp += arr[j][1] * arr[j][0]
                res.append(temp)
                cnt[nums[i-k+1]] -= 1
        return res


nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2
output = [6, 10, 12]


obj = Solution()
res = obj.findXSum(nums, k, x)
print(res)
print(output)
print(res == output)
