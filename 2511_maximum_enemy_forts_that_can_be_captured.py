class Solution:
    def captureForts(self, forts: list[int]) -> int:
        n = len(forts)

        def capture(start, stop, step):
            res = 0
            cur = 0
            capturing = False
            for i in range(start, stop, step):
                if forts[i] == 1:
                    cur = 0
                    capturing = True
                elif forts[i] == 0 and capturing:
                    cur += 1
                else:
                    res = max(cur, res)
                    capturing = False
            return res

        return max(capture(0, n, 1), capture(n-1, -1, -1))


forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
output = 4

obj = Solution()
res = obj.captureForts(forts)
print(res)
print(output)
print(res == output)
