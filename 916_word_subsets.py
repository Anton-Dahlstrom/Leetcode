class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def findSubset(word, hmapcopy):
            for char in word:
                if char not in hmapcopy or hmapcopy[char] == 0:
                    return False
                hmapcopy[char] -= 1
            return True

        res = []
        for w1 in words1:
            hmap = {}
            for char1 in w1:
                hmap.setdefault(char1, 0)
                hmap[char1] += 1
                stopped = False
            for w2 in words2:
                hmapcopy = hmap.copy()
                if not findSubset(w2, hmapcopy):
                    stopped = True
                    break
            if not stopped:
                res.append(w1)

        return res


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
output = ["facebook", "google", "leetcode"]

obj = Solution()
res = obj.wordSubsets(words1, words2)
print(res)
print(output)
print(res == output)
