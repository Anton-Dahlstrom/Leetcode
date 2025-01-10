class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        hmap = {}
        for word2 in words2:
            temp = {}
            for char in word2:
                temp.setdefault(char, 0)
                temp[char] += 1
            for key in temp:
                hmap.setdefault(key, 0)
                hmap[key] = max(hmap[key], temp[key])

        def checkSubset(hmap, word):
            for char in word:
                if char in hmap:
                    hmap[char] -= 1
                    if hmap[char] == 0:
                        hmap.pop(char)
            if hmap:
                return False
            return True

        res = []
        for word1 in words1:
            temp = hmap.copy()
            if checkSubset(temp, word1):
                res.append(word1)

        return res


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
output = ["facebook", "google", "leetcode"]

obj = Solution()
res = obj.wordSubsets(words1, words2)
print(res)
print(output)
print(res == output)
