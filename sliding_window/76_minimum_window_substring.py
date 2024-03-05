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
        l = 0
        r = 0
        substr = {}
        chars = {}
        for char in t:
            chars[char] = 0
            substr[char] = 1 + substr.get(char, 0)

        unique = len(t)
        found = 0
        startChar = ""
        shortest = 0
        finalstr = [0]
        while r < len(s):
            char = s[r]
            if char in chars:
                if found < unique:
                    if not found:
                        startChar = char
                    chars[char] += 1
                    if chars[char] <= substr[char]:
                        found += 1
                        if found == unique:
                            shortest = r + 1
                            finalstr = [l, r]
                            while chars[startChar] > substr[startChar]:
                                l += 1
                                lchar = s[l]
                else:
                    if char != startChar:
                        chars[char] += 1
                    else:
                        while l < r:
                            l += 1
                            lchar = s[l]
                            if lchar in chars:
                                if chars[lchar] > substr[lchar]:
                                    chars[lchar] -= 1
                                else:
                                    startChar = lchar
                                    shortest = min(r - l + 1, shortest)
                                    if r - l + 1 < shortest:
                                        finalstr = [l, r]
                                        shortest = r - l + 1
                                    break
            r += 1
        result = s[finalstr[0]: finalstr[1]+1]
        return result


obj = Solution()
result = obj.minWindow(s, t)
print(result)
