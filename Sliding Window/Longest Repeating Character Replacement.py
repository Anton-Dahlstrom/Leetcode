s = "ABAB" 
k = 2

# s = "AABABBA" 
# k = 1

# s = "BAAA"
# k = 0
# answer: 3

s = "aABBB"
k = 2
# 4
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter = ""
        skips = k
        counter = 0
        longest = 0
        nextIndex = 0
        i = 0
        while i < len(s):
            char = s[i]
            if not letter:
                letter = char
                counter += 1
                i += 1
                continue
            if char != letter:
                if skips == k:
                    nextIndex = i
                if skips:
                    skips -= 1
                    counter += 1
                else:
                    if nextIndex:
                        i = nextIndex-1
                        lastIndex = nextIndex
                        nextIndex = 0
                    letter = ""
                    longest = max(counter, longest)
                    counter = 0
            else:
                counter += 1
                longest = max(counter, longest)
            i += 1

        if k:
            print(lastIndex, "HERE")
            print(counter)
            print("hi")
            for char in s[lastIndex::-1]:
                print(counter)
                counter += 1
                if char != letter:
                    k -= 1
                    if k == 0:
                        break
        longest = max(counter, longest)
        return longest
        
obj = Solution()
answer = obj.characterReplacement(s, k)
print(answer)

