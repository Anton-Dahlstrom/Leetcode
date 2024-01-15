s = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        temp = ""
        longest = 0
        for i, char in enumerate(s):
            if char in temp:
                for j, letter in enumerate(temp):
                    temp = temp.replace(letter, "", 1)
                    if letter == char:
                        break
            temp += char
            longest = max(len(temp), longest)
        return longest
    
obj = Solution()
answer = obj.lengthOfLongestSubstring(s)
print(answer)
