class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        evens = 0
        oddevens = 0
        odds = 0
        res = 0

        for i in reversed(range(n)):
            if arr[i] % 2 == 0:
                if odds % 2 == 0:
                    evens += 1
                else:
                    oddevens += 1
                res += (odds+1)//2
            else:
                res += odds//2
                res += 1
                odds += 1

            if not odds:
                continue

            if odds % 2 == 0:
                res += oddevens
            else:
                res += evens
        return res % (10**9 + 7)


arr = [1, 2, 3, 4, 5, 6, 7]
output = 16

obj = Solution()
res = obj.numOfSubarrays(arr)
print(res)
print(output)
print(res == output)
