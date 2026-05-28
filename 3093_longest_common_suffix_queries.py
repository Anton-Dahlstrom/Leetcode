from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # char: [{}, smallest, index]
        trie = {}
        minsize = float("inf")
        defaultres = -1
        for i, word in enumerate(wordsContainer):
            cur = trie
            size = len(word)
            if size < minsize:
                minsize = size
                defaultres = i
            for char in reversed(word):
                if char in cur:
                    if size < cur[char][1]:
                        cur[char][1] = size
                        cur[char][2] = i
                else:
                    cur[char] = [{}, size, i]
                cur = cur[char][0]

        res = []
        for word in wordsQuery:
            cur = trie
            temp = defaultres
            test = 0
            for char in reversed(word):
                if char in cur:
                    temp = cur[char][2]
                    cur = cur[char][0]
                else:
                    break
            res.append(temp)
        return res
