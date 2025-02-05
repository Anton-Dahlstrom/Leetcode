class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        needfrom1 = ""
        needfrom2 = ""
        match = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if match:
                    return False
                if not needfrom1:
                    needfrom1 = s2[i]
                    needfrom2 = s1[i]
                else:
                    if s2[i] != needfrom2 or s1[i] != needfrom1:
                        return False
                    else:
                        match = True

        return match or needfrom1 == ""


s1 = "bank"
s2 = "kanb"
output = True

obj = Solution()
res = obj.areAlmostEqual(s1, s2)
print(res)
print(output)
print(res == output)
