class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {"a", "i", "e", "o", "u"}
        words = s.split(" ")
        n = len(words)

        def countVowels(word):
            cnt = 0
            for char in word:
                if char in vowels:
                    cnt += 1
            return cnt
        target = countVowels(words[0])

        for i in range(1, n):
            if countVowels(words[i]) == target:
                words[i] = words[i][::-1]

        return " ".join(words)


s = "cat and mice"
output = "cat dna mice"

obj = Solution()
res = obj.reverseWords(s)
print(res)
print(output)
print(res == output)
