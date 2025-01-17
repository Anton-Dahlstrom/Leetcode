class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def addJustified(arr):
            spaces = len(arr) - 1
            chars = maxWidth - size
            default = chars//spaces if spaces else 0
            extra = chars % spaces if spaces else 0
            res = ""
            for i in range(spaces):
                res += arr[i] + " "*default
                if i <= extra-1:
                    res += " "
            res += arr[-1]
            return res

        def addNonjustified(arr, size):
            return " ".join(arr) + " "*(maxWidth-size-len(temp)+1)

        size = 0
        temp = []
        res = []
        for word in words[:len(words)-1]:
            if size + len(word) + len(temp) > maxWidth:
                if len(temp) > 1:
                    res.append(addJustified(temp))
                else:
                    res.append(addNonjustified(temp, size))
                temp = []
                size = 0
            temp.append(word)
            size += len(word)
        if size + len(words[-1]) + len(temp) > maxWidth:
            if len(temp) > 1:
                res.append(addJustified(temp))
            else:
                res.append(addNonjustified(temp, size))
            size = 0
            temp = []
        temp.append(words[-1])
        size += len(words[-1])
        res.append(addNonjustified(temp, size))
        return res


words = ["Here", "is", "an", "example", "of", "text", "justification."]
maxWidth = 14
output = ["Here   is   an", "example     of",
          "text          ", "justification."]

obj = Solution()
res = obj.fullJustify(words, maxWidth)
print(res)
print(output)
print(res == output)
