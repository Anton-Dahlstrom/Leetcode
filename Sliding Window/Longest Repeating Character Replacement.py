s = "ABAB" 
k = 2

s = "AABABBA" 
k = 1

# s = "BAAA"
# k = 0
# answer: 3

# s = "aBBB"
# k = 2
# 4
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {} # Index, count
        overCapacity = False
        longest = 0
        current = 0
        i = 0
        mainLetter = ""
        # Maybe just keep track of the largest?
        while i < len(s):
            print(i)
            char = s[i]
            if letters.get(char):
                letters[char][1] += 1
                if letters[char][1] > k:
                    if not overCapacity:
                        mainLetter = char
                        overCapacity = True
                    else:
                        del letters[mainLetter]
                        mainLetter = ""
                        i = letters[min(letters, key=letters.get)][0]
                        letters = {}
                        overCapacity = False
                        longest = max(current, longest)
                        current = 0
                        print(letters)
                        continue
            else:
                letters[char] = [i, 1]
            current += 1
            i += 1
        longest = max(longest, current)
        return longest


obj = Solution()
answer = obj.characterReplacement(s, k)
print(answer)

# asd = {"a": [2, 5], "d": [1, 500]}
# asd2 = max(asd, key=asd.get)
# print(asd2)