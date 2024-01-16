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
        letters = {} # Index, count
        capacity = k
        overCapacity = False
        longest = 0
        i = 0
        # Maybe just keep track of the largest?
        while i < len(s):
            char = s[i]
            if letters.get(char):
                letters[char] += 1
                if letters[char] > k:
                    if not overCapacity:
                        overCapacity = True
                    else:
                        pass # move i to the next index
                        overCapacity = False
            else:
                letters[char] = 1


obj = Solution()
answer = obj.characterReplacement(s, k)
print(answer)

asd = {"a": 4, "d": 8}
print(asd[max(asd)])