# Premium problem solved on neetcode.

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Keeps track of where to start when we return the result.
        roots = set()
        edges = {}
        backward = {}
        chars = set()
        irrationalOrder = False

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
                        break  # Should this break?
                    if cur in backward:
                        parentArr += [p for p in backward[cur]
                                      if p not in visited]

        def removeCommonChild(before, after):
            if before in edges and after in edges:
                beforeChild = edges[before]
                visited = set()
                childArr = [after]
                while childArr:
                    cur = childArr.pop()
                    visited.add(cur)
                    if cur in beforeChild:
                        backward[cur].remove(before)
                        beforeChild.remove(cur)
                        break
                    if cur in edges:
                        childArr += [c for c in edges[cur] if c not in visited]

        for i in range(len(words)):
            madeEdge = False
            for j in range(len(words[i])):
                # Looks for the index of the first different character between two words
                if words[i][j] not in chars:
                    chars.add(words[i][j])
                if not madeEdge and i > 0:
                    if j < len(words[i-1]) and j < len(words[i]):
                        if words[i-1][j] != words[i][j]:
                            before, after = words[i-1][j], words[i][j]
                            madeEdge = True

                            # Removes unnecessary edges if Afters direct parent is also a parent of before.
                            removeCommonParent(before, after)
                            removeCommonChild(before, after)

                            # Adds connections to edges and backwards
                            edges.setdefault(before, set()).add(after)
                            backward.setdefault(after, set()).add(before)

                            if before not in backward:
                                roots.add(before)
                            if after in roots:
                                roots.remove(after)

            if not madeEdge and i > 0:
                if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                    irrationalOrder = True

        self.looping = False

        # Need to fix function so it detects loops and can work with two starting roots.
        def createResult(cur: set, visited: set):
            res = ""
            for char in cur:
                if char in visited:
                    print(char)
                    self.looping = True
                    return ""
                if char in chars:
                    chars.remove(char)
                    res += char
                if char in edges:
                    visited.update(char)
                    res += createResult(edges[char], visited)
            return res
        res = createResult(roots, set())
        unused = "".join([c for c in chars])
        if self.looping:
            return ""
        if (edges and not res) or (not res and irrationalOrder):
            return ""
        return unused + res


words = ["ab", "ad", "adc", "add", "addb", "addc", "b"]
output = "abcd"


obj = Solution()
res = obj.foreignDictionary(words)
print(res)
print(res == output)
