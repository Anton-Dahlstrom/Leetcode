
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        n = len(digits)

        res = set()
        used = []

        def dfs(size):
            if size == 3:
                res.add("".join([str(digits[index]) for index in used]))
                return 1
            for i in range(0, n):
                if size == 0 and digits[i] == 0:
                    continue
                if size == 2 and digits[i] % 2 != 0:
                    continue
                if i in used:
                    continue
                used.append(i)
                dfs(size+1)
                used.pop()
        dfs(0)
        return len(res)


digits = [1, 2, 3, 4]
output = 12


obj = Solution()
res = obj.totalNumbers(digits)
print(res)
print(output)
print(res == output)
