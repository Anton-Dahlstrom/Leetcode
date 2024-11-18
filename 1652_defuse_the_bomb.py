class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        res = [0] * len(code)
        if not k:
            return res

        start = 1
        if k < 0:
            start = -1

        for i in range(len(code)):
            for j in range(i+start, i + k+start, start):
                index = j % len(code)
                res[i] += code[index]
        return res


code = [5, 7, 1, 4]
k = 3
output = [12, 10, 16, 13]

obj = Solution()
res = obj.decrypt(code, k)
print(res)
print(output)
print(res == output)
