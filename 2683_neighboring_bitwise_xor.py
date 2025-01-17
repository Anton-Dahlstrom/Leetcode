class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        res = [0] * len(derived)
        for i in range(1, len(derived)):
            if derived[i] == 1:
                res[i] = abs(res[i-1]-1)
            else:
                res[i] = res[i-1]
        if derived[0] == res[0] ^ res[-1]:
            return True
        return False


derived = [1, 1, 0]
output = True


obj = Solution()
res = obj.doesValidArrayExist(derived)
print(res)
print(output)
print(res == output)
