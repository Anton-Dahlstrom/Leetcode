class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        i = 0
        nodes = {}
        while True:
            prev = ""
            toPop = []
            for index, word in enumerate(words):
                if i >= len(word):
                    toPop.append(index)
                    continue

                # Need to only confirm relationship between characters if all previous
                # characters match.
                if prev and prev != word[i]:
                    nodes[prev] = word[i]
                prev = word[i]
            for index in toPop[::-1]:
                words.pop(index)
            i += 1
            if not prev:
                break


words = ["hrn", "hrf", "er", "enn", "rfnn"]
output = "hernf"

obj = Solution()
res = obj.foreignDictionary(words)
print(res)
print(res == output)
