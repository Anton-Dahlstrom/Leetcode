class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        common_chars = set1.intersection(text2)
        text1 = "".join(char for char in text1 if char in common_chars)
        text2 = "".join(char for char in text2 if char in common_chars)
        if not text1 or not text2:
            return 0

        array = [0]*len(text2)
        hmap = {}
        for i, char in enumerate(text2):
            hmap.setdefault(char, []).append(i)
        print(text2)
        print(hmap)

        for char in text1[::-1]:
            print(array)
            if not hmap[char]:
                continue
            index = hmap[char][-1]
            val = 0
            if index < len(array)-1:
                val = max(array[index+1:])
            print(index, char)
            print(hmap)
            # if val > array[index]:
            #     array[index] = val+1
            #     hmap[char].pop()
            array[index] = max(array[index], val+1)
        print(text1)
        print(text2)
        print(array)
        return max(array)

        # yqpqaar
        # yraqp
        # r = 1, start = 6, 1
        # a = 1, start = 5, 2
        # a = 1, start = 4, 2
        # q = 1, start = 3, 3
        # p = 1, start = 2, 4
        # q = 2, start = 1, 3
        # y = 3, start = 0, 0


text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
# yqp
output = 3

text1 = "abcba"
text2 = "abcbcba"
output = 5

text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
output = 3

obj = Solution()
res = obj.longestCommonSubsequence(text1, text2)
print(res)
print(res == output)
