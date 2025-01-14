class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        i = 0
        prefix = [0] * len(A)
        achars = set()
        bchars = set()
        common = set()
        while i < len(A):
            if A[i] not in common:
                if A[i] in bchars:
                    bchars.remove(A[i])
                    common.add(A[i])
                else:
                    achars.add(A[i])
            if B[i] not in common:
                if B[i] in achars:
                    achars.remove(B[i])
                    common.add(B[i])
                else:
                    bchars.add(B[i])
            prefix[i] = len(common)
            i += 1
        return prefix


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
output = [0, 2, 3, 4]

obj = Solution()
res = obj.findThePrefixCommonArray(A, B)
print(res)
print(output)
print(res == output)
