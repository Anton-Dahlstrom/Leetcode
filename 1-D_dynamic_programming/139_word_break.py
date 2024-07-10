from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        temp = [word for word in wordDict if word[0] == s[0]]
        for char in s:
            ending = False
            if not temp:
                return False
            for i in reversed(range(0, len(temp))):
                if temp[i][0] == char:
                    if temp[i][1:]:
                        temp[i] = temp[i][1:]
                    else:
                        temp.pop(i)
                        ending = True
                else:
                    temp.pop(i)
            if ending:
                temp += wordDict
        if ending:
            return True
        return False


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
output = False

s = "aaaaaaa"
wordDict = ["aaaa", "aa"]
output = False

obj = Solution()
res = obj.wordBreak(s, wordDict)
print(res)
print(res == output)
