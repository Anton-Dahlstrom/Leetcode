class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        state = 0
        cnt = [0]*(1 << 11)
        cnt[0] = 1
        for char in word:
            bit = ord(char)-96
            bit = 1 << bit
            state ^= bit
            res += cnt[state]
            for oddBit in range(1, 11):
                temp = state ^ (1 << oddBit)
                res += cnt[temp]
            cnt[state] += 1

        return res


word = "aabb"
output = 9

# word = "aa"
# output = 3

word = "ab"
output = 2

obj = Solution()
res = obj.wonderfulSubstrings(word)
print(res)
print(output)
print(res == output)
