class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        visited = set()

        def dfs(p1, p2):
            if (p1, p2) in visited:
                return
            visited.add((p1, p2))
            print(p1, p2)
            p3 = p1 + p2
            if p3 == len(s3):
                return True
            if p1 < len(s1) and s1[p1] == s3[p3]:
                if dfs(p1+1, p2):
                    return True
            if p2 < len(s2) and s2[p2] == s3[p3]:
                if dfs(p1, p2+1):
                    return True
            return False
        return dfs(0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
output = True


s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

obj = Solution()
res = obj.isInterleave(s1, s2, s3)
print(res)
print(res == output)
