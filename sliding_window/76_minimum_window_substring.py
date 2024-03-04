s = "ADOBECODEBANC"
t = "ABC"
Output = "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


# Iterate through the string with the pointer until we find all the chars in t.
# The only way to make the substring shorter is to find a duplicate of the first char we found.
# We save the relevant chars in a stack containing the chars value and their index and the count of each char in
# our hmap with char values. 
# When the pointer finds a duplicate of the char at the bottom of the stack we pop it from the stack and 
# reduce it's value in the hashmap by 1. We continue trying to pop from the bottom of the stack by checking if
# the value of the char at the bottom is > 1 in our hmap.
# If not we calculate the difference between the index of the char we couldn't pop from the stack and our pointer.
# We then compare that with the smallest substring we found so far. Continue until the value of the pointer is greater
# than the length of the string.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        chars = {}
        for char in t:
            chars[char] = 0
        unique = len(t)
        found = 0 
        while r < len(s):
            if found < unique:
                r += 1
            else:
                l += 1
            if s[r] in chars:





obj = Solution()
result = obj.minWindow(s, t)
print(result)
