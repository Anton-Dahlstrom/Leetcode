class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        charStart, charEnd = ord("a"), ord("z")

        if len(word) < 3:
            return False
        vowel, consonant = False, False
        for i in range(len(word)):
            if word[i].isdigit():
                continue
            char = word[i].lower()
            if ord(char) in range(charStart, charEnd+1):
                if char in vowels:
                    vowel = True
                else:
                    consonant = True
            else:
                return False

        return vowel and consonant


word = "234Adas"
output = True

obj = Solution()
res = obj.isValid(word)
print(res)
print(output)
print(res == output)
