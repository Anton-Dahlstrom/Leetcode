from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = {}
        for word in dictionary:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]

        def dfs(word, i, skipped, hmap):
            if skipped == 3:
                return False
            if i == len(word):
                return True
            for char in hmap:
                if char == word[i]:
                    if dfs(word, i+1, skipped, hmap[char]):
                        return True
                else:
                    if dfs(word, i+1, skipped+1, hmap[char]):
                        return True
            return False

        res = []
        for word in queries:
            if dfs(word, 0, 0, trie):
                res.append(word)
        return res
