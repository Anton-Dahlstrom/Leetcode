class Solution:
    def maxProduct(self, words: list[str]) -> int:
        words.sort(reverse=True, key=lambda k: len(k))
        words = [(len(word), set(word)) for word in words]
        i = 0

        res = 0
        while i < len(words)-1:
            j = i
            while j < len(words):
                l1, u1 = words[i]
                l2, u2 = words[j]
                if l1 * l2 < res:
                    break
                expected = len(u1) + len(u2)
                j += 1
                if len(u1.union(u2)) < expected:
                    continue
                res = max(res, l1*l2)
            i += 1
        return res


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
output = 16

obj = Solution()
res = obj.maxProduct(words)
print(res)
print(output)
print(res == output)
