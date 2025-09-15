class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        res = 0
        for word in text.split(" "):
            valid = True
            for char in word:
                if char in broken:
                    valid = False
                    break
            if valid:
                res += 1

        return res


text = "hello world"
brokenLetters = "ad"
output = 1

obj = Solution()
res = obj.canBeTypedWords(text, brokenLetters)
print(res)
print(output)
print(res == output)
