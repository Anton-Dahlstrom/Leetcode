class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0
        n = len(word)
        vowels = {"a", "e", "o", "i", "u"}
        l = 0
        r = 0
        consonants = 0
        vowelcount = {}
        prefix = [0]*n
        cnt = 1
        for i in range(n-1, -1, -1):
            prefix[i] = cnt
            if word[i] in vowels:
                cnt += 1
            else:
                cnt = 1

        while r < n:
            if consonants == k and len(vowelcount) == 5:
                res += prefix[r-1]

            if (consonants < k or len(vowelcount) < 5):
                cur = word[r]
                if cur in vowels:
                    if cur in vowelcount:
                        vowelcount[cur] += 1
                    else:
                        vowelcount[cur] = 1
                else:
                    consonants += 1
                r += 1

            else:
                cur = word[l]
                if cur in vowels:
                    vowelcount[cur] -= 1
                    if vowelcount[cur] == 0:
                        vowelcount.pop(cur)
                else:
                    consonants -= 1
                l += 1
                r = max(l, r)

        while consonants >= k and len(vowelcount) == 5:
            if consonants == k:
                res += 1
            cur = word[l]
            if cur in vowels:
                vowelcount[cur] -= 1
                if vowelcount[cur] == 0:
                    vowelcount.pop(cur)
            else:
                consonants -= 1
            l += 1

        return res


word = "iqeaouqi"
k = 2
output = 3


obj = Solution()
res = obj.countOfSubstrings(word, k)
print(res)
print(output)
print(res == output)
