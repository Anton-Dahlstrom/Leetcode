class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            print(word[:len(searchWord)])
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1

sentence = "i love eating burger"
searchWord = "burg"
output = 4

obj = Solution()
res = obj.isPrefixOfWord(sentence, searchWord)
print(res)
print(output)
print(res == output)