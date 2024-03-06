s = "ADOBECODEBANC"
t = "ABC"
Output = "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


# Iterate through the string with the pointer until we find all the chars in t.
# TO DO: Move left as much as you can without breaking the substring

# The only way to make the substring shorter is to find a duplicate of the first char we found.
# Find the duplicate with the right pointer then move left as much as you can again.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        neededChars = {}
        currentChars = {}
        temp = {}

        for char in t:
            currentChars[char] = 0
            neededChars[char] = 1 + neededChars.get(char, 0)
            temp[char] = 1 + temp.get(char, 0)

        l = 0
        startChar = ""
        length = len(s)
        while l < length:
            char = s[l]
            if char in neededChars:
                currentChars[char] += 1
                startChar = char
                break
            else:
                l += 1
        print(startChar)

        r = l + 1
        while temp and r < length:
            print(temp)
            char = s[r]
            if char in neededChars:
                currentChars[char] += 1
                if char in temp:
                    temp[char] -= 1
                    if temp[char] == 0:
                        temp.pop(char)
            r += 1

        if temp:
            return ""
        shortest = r - l + 1
        indexes = [l, r]
        print(shortest)
        expand = True
        while True:
            if expand:
                r += 1
                if r >= length:
                    break
                char = s[r]
                if char == startChar:
                    expand = False
            else:
                l += 1
                char = s[l]
                if char in currentChars:
                    if currentChars[char] > neededChars:
                        currentChars[char] -= 1
                    else:
                        startChar = char
                        expand = True
                        cur = r - l + 1
                        if cur < shortest:
                            shortest = cur
                            indexes = [l, r]
        print(indexes)
        return s[indexes[0]: indexes[1]+1]


obj = Solution()
result = obj.minWindow(s, t)
print(result)
