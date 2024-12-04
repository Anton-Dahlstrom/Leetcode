class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # ord: a = 97, z = 122

        def dfs(i1, i2):
            if i2 == len(str2):
                return True
            if i1 == len(str1):
                return False

            ord1, ord2 = ord(str1[i1]), ord(str2[i2])
            if ord1 == ord2 or ord1+1 == ord2 or (ord1 == 122 and ord2 == 97):
                if dfs(i1+1, i2+1):
                    return True
            else:
                return dfs(i1+1, i2)
            return False

        return dfs(0, 0)


str1 = "abc"
str2 = "ad"
output = True

obj = Solution()
res = obj.canMakeSubsequence(str1, str2)
print(res)
print(output)
print(res == output)
