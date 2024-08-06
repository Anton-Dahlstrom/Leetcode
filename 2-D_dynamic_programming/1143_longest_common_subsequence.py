class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        common_chars = set1.intersection(text2)
        text1 = "".join(char for char in text1 if char in common_chars)
        text2 = "".join(char for char in text2 if char in common_chars)
        print(text1)
        print(text2)
        hmap1 = {}
        hmap2 = {}
        for i, char in enumerate(text1):
            hmap1.setdefault(char, []).append(i)
        for i, char in enumerate(text2):
            hmap2.setdefault(char, []).append(i)

        # yqpqaar
        # yraqp
        # r = 1, start = 6, 1
        # a = 2, start = 5, 2
        # a = 2, start = 4, 2
        # q = 1, start = 3, 3
        # p = 1, start = 2, 4
        # q = 2, start = 1, 3
        # y = 3, start = 0, 0
        print(hmap1)
        print(hmap2)


text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
# yqp
output = 3

obj = Solution()
res = obj.longestCommonSubsequence(text1, text2)
print(res)
print(res == output)
