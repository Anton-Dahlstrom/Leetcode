class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        res = 0
        for op in operations:
            if op[0] == "+" or op[-1] == "+":
                res += 1
            else:
                res -= 1
        return res


operations = ["--X", "X++", "X++"]
output = 1

obj = Solution()
res = obj.finalValueAfterOperations(operations)
print(res)
print(output)
print(res == output)
