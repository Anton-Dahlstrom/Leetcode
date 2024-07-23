class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        edges = set(wordList)
        if endWord not in edges:
            return 0

        edges = {beginWord: []}
        totalDiff = 0
        for c in range(len(beginWord)):
            if beginWord[c] != endWord[c]:
                totalDiff += 1

        for word in wordList:
            diff = 0
            for c in range(len(beginWord)):
                if word[c] != beginWord:
                    diff += 1
                    if diff > totalDiff:
                        continue

            edges.setdefault(word, [])
            for edge in edges:
                miss = 0
                for i in range(len(word)):
                    if word[i] != edge[i]:
                        miss +=1
                        if miss > 1:
                            continue
                if miss == 1:
                    edges[edge].append(word)
                    edges[word].append(edge)


        self.shortest = float("inf")
        old = set()
        next = set([endWord])
        steps = 1

        while next:
            if beginWord in next:
                return steps
            temp = set()
            steps += 1
            for val in next:
                for word in edges[val]:
                    if (word not in old and
                        word not in next and
                            word not in temp):
                        temp.add(word)
            old.update(next)
            next = temp

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
output = 5

beginWord = "qa"
endWord = "sq"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb",
            "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
output = 5


obj = Solution()
res = obj.ladderLength(beginWord, endWord, wordList)
print(res)
print(res == output)
