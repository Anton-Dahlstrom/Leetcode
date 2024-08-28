class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Keeps track of where to start when we return the result.
        roots = set()
        edges = {}
        backward = {}
        # Need to remove common children.
        # Is the direct child of Before a child of after?

        def removeCommonParent(before, after):
            if after in backward and before in backward:
                afterParents = backward[after]
                visited = set()
                parentArr = [before]
                while parentArr:
                    cur = parentArr.pop()
                    visited.add(cur)
                    if cur in afterParents:
                        edges[cur].remove(after)
                        afterParents.remove(cur)
                        break
                    if cur in backward:
                        parentArr += [p for p in backward[cur]
                                      if p not in visited]

        for i in range(1, len(words)):
            j = 0
            # Looks for the index of the first different character between two words
            while j < len(words[i-1]) and j < len(words[i]) and words[i-1][j] == words[i][j]:
                j += 1
            if j < len(words[i-1]) and j < len(words[i]):
                before, after = words[i-1][j], words[i][j]

                # Removes unnecessary edges if Afters direct parent is also a parent of before.
                removeCommonParent(before, after)
                # Adds connections to edges and backwards
                edges.setdefault(before, set()).add(after)
                backward.setdefault(after, set()).add(before)

                if before not in backward:
                    roots.add(before)
                if after in roots:
                    roots.remove(after)

        return


words = ["hrn", "hrf", "er", "enn", "rfnn"]
output = "hernf"
words = ["ab", "ad", "adc", "add", "addb", "addc", "b"]
output = "abcd"

obj = Solution()
res = obj.foreignDictionary(words)
print(res)
print(res == output)
