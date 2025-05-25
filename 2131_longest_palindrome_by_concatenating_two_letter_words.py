from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        dict = defaultdict(int)
        res = 0
        mids = 0
        words.sort()
        for word in words:
            s, e = word[0], word[1]
            if dict[(e, s)]:
                res += 4
                dict[(e, s)] -= 1
                if s == e:
                    mids -= 1
            else:
                dict[(s, e)] += 1
                if s == e:
                    mids += 1

        if mids:
            res += 2

        return res


words = ["ab", "ty", "yt", "lc", "cl", "ab"]
output = 8

words = ["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf",
         "of", "of", "oo", "of", "of", "qf", "qf", "of"]
output = 14

obj = Solution()
res = obj.longestPalindrome(words)
print(res)
print(output)
print(res == output)
