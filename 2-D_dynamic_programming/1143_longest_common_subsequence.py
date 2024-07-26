class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [0, 0]
        set1 = set(text1)
        hmap2 = {}
        for i, char in enumerate(text2):
            if char in set1:
                hmap2.setdefault(char, []).append(i)

        for j in reversed(range(len(text1))):
            char = text1[j]
            if text1[j] in hmap2:
                if not res[0]:
                    res[0] = 1
                    res[1] = hmap2[char].pop()
                elif res[0] == 1 and hmap2[char][-1] > res[1]:
                    res[1] = hmap2[char].pop()
                elif hmap2[char][-1] < res[1]:
                    res[0] += 1
                    res[1] = hmap2[char].pop()

                if not hmap2[char]:
                    hmap2.pop(char)

        return res[0]


text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
# qpaar
# raqp

output = 3

obj = Solution()
res = obj.longestCommonSubsequence(text1, text2)
print(res)
print(res == output)
