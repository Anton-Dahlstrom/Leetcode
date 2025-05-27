class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divsum = 0
        nondivsum = 0
        for i in range(n+1):
            if i % m:
                nondivsum += i
            else:
                divsum += i
        return nondivsum - divsum


n = 10
m = 3
output = 19

obj = Solution()
res = obj.differenceOfSums(n, m)
print(res)
print(output)
print(res == output)
