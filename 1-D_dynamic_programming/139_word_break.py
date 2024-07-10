from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s and not wordDict:
            return False
        temp = []
        print(wordDict, s)
        wordEnding = False
        for char in s:
            tempEnding = False
            found = False
            for i in reversed(range(0, len(temp))):
                if temp[i][0] == char:
                    found = True
                    if temp[i][1:]:
                        temp[i] = temp[i][1:]
                    else:
                        tempEnding = True
                else:
                    print("True")
                    tempEnding = True
                    temp.pop(i)
            if tempEnding or wordEnding or not temp:
                wordEnding = False
                for word in wordDict:
                    if word[0] == char:
                        found = True
                        if word[1:]:
                            temp.append(word[1:])
                        else:
                            wordEnding = True
            if not found:
                return False
            print(char, temp)
        print(tempEnding, wordEnding)
        if tempEnding or wordEnding:
            return True
        return False


s = "leetcode"
wordDict = ["leet", "code"]
output = True

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
output = False

# s = "a"
# wordDict = ["a"]
# output = True

# s = "a"
# wordDict = ["b"]

# s = "abcd"
# wordDict = ["a", "abc", "b", "cd"]
# output = True

# s = "aaaaaaa"
# wordDict = ["aaaa", "aa"]

obj = Solution()
res = obj.wordBreak(s, wordDict)
print(res)

# asd = []
# a = "abcd"
# asd.append(a[4:])
# print(asd)
