class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        print(s)
        wordDict = {}
        wordLen = 0
        wordLenTotal = 0
        res = []

        for word in words:
            if not wordLenTotal:
                wordLen = len(word)
                wordLenTotal = len(word) * len(words)
            wordDict[word] = wordDict.setdefault(word, 0) + 1


        for i in range(len(s) - wordLenTotal + 1):
            j = i
            if s[j:j+wordLen] in wordDict:
                wordDictCopy = wordDict.copy()
                word = s[j:j+wordLen]
                while word in wordDictCopy:
                    wordDictCopy[word] -= 1
                    if wordDictCopy[word] < 0:
                        break
                    j += wordLen 
                    word = s[j:j+wordLen]
                if j - i == wordLenTotal:
                    res.append(i)                    

        return res

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
output = [8]

obj = Solution()
res = obj.findSubstring(s, words)
print(res)
print(output)
print(res == output)
