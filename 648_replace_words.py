class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = {}
        for key in dictionary:
            cur = trie
            for char in key:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[1] = True
        res = []
        for word in sentence.split(" "):
            cur = trie
            i = 0
            while i < len(word):
                char = word[i]
                if 1 in cur:
                    res.append(word[:i])
                    break
                if char not in cur:
                    res.append(word)
                    break
                cur = cur[char]
                i += 1
            if i == len(word):
                res.append(word)

        return " ".join(res)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
output = "the cat was rat by the bat"

obj = Solution()
res = obj.replaceWords(dictionary, sentence)
print(res)
print(output)
print(res == output)
