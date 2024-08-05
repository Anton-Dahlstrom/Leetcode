class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        both = set()
        hmap1 = {}
        hmap2 = {}
        for char in text2:
            if char in set1:
                both.add(char)
        text1 = "".join([char for char in text1 if char in both])
        text2 = "".join([char for char in text2 if char in both])
        for i, char in enumerate(text1):
            hmap1.setdefault(char, []).append(i)
        for i, char in enumerate(text2):
            hmap2.setdefault(char, []).append(i)

        print(hmap1)
        print(hmap2)


text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"

output = 3

obj = Solution()
res = obj.longestCommonSubsequence(text1, text2)
print(res)
print(res == output)
