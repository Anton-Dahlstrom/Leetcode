class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n:
            if bits[i] == 1 and i < n-1:
                bits[i+1] = 1
                i += 1
            i += 1

        return bits[-1] == 0


bits = [1, 1, 1, 0]
output = False

obj = Solution()
res = obj.isOneBitCharacter(bits)
print(res)
print(output)
print(res == output)
