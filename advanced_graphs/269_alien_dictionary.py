class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Keeps track of where to start when we return the result.
        root = ""

        edges = {}
        backward = {}

        groups = []

        for i in range(1, len(words)):
            j = 0
            # Looks for the index of the first different character between two words
            while j < len(words[i-1]) and j < len(words[i]) and words[i-1][j] == words[i][j]:
                j += 1
            if j < len(words[i-1]) and j < len(words[i]):
                before, after = words[i-1][j], words[i][j]

                # Manages groups of characters to prune connections making sure each
                # character only has one child by the end.
                if before not in backward and before not in edges:
                    # Neither character has been added before so we make a new group.
                    if after not in backward and after not in edges:
                        groups.append(set([before, after]))
                    # After is part of a group so we add before to the group
                    else:
                        for group in groups:
                            if after in group:
                                group.add(before)
                                break
                else:
                    # Before is part of a group but after isn't so we add after to the group.
                    if after not in backward and after not in edges:
                        for group in groups:
                            if before in group:
                                group.add(after)
                                break
                    # Both characters are part of different groups so we combine them.
                    else:
                        for i, group in enumerate(groups):
                            beforeGroup = None
                            afterGroup = None
                            if before and after in group:
                                break
                            if before in group:
                                beforeGroup = i
                                if afterGroup:
                                    break
                            if after in group:
                                afterGroup = i
                                if beforeGroup:
                                    break
                        if beforeGroup and afterGroup:
                            groups[beforeGroup].update(groups[afterGroup])
                            groups.pop(afterGroup)

                # Adds connections to edges and backwards
                edges.setdefault(before, []).append(after)
                backward.setdefault(after, []).append(before)
                if before not in backward:
                    root = before
        print(groups)
        print(edges)
        print(backward)
        print(root)
        return


words = ["hrn", "hrf", "er", "enn", "rfnn"]
output = "hernf"
words = ["ab", "ad", "adc", "add", "addb", "addc", "b"]
output = "abcd"
# abcd
# a > b = ab
# b > d = abd
# c > d = cabd
# b > c = abcd

obj = Solution()
res = obj.foreignDictionary(words)
print(res)
print(res == output)

# asd = set([1, 5])
# asd2 = set([2, 3])
# asd.update(asd2)
# print(asd)
