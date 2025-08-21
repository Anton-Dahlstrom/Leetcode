class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)
        res = 0
        for l in range(n):
            r = l
            temp = set()
            while r < n and word[r] in vowels:
                temp.add(word[r])
                if len(temp) == 5:
                    res += 1
                r += 1
        return res


word = "unicornarihan"
output = 0

word = "cuaieuouac"
output = 7

obj = Solution()
res = obj.countVowelSubstrings(word)
print(res)
print(output)
print(res == output)
