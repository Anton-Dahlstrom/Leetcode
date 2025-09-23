class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        n = max(len(v1), len(v2))
        for i in range(n):
            val1, val2 = 0, 0
            if i < len(v1):
                val1 = int(v1[i])
            if i < len(v2):
                val2 = int(v2[i])
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1

        return 0


version1 = "1.2"
version2 = "1.10"
output = -1

obj = Solution()
res = obj.compareVersion(version1, version2)
print(res)
print(output)
print(res == output)
