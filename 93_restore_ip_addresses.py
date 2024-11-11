class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) < 4:
            return res

        def dfs(s, i, needed):
            # Confirm the last number of the ip-address isn't greater than 255 or a number with 2+ digits that start with a zero.
            if not needed:
                if int(s[i:]) > 255 or (len(s)-i > 1 and s[i] == "0"):
                    return
                res.append(s)
                return
            # If this number starts with 0 we can't add more digits to it.
            if s[i] == "0" and len(s) - i > 1:
                dfs(s[:i+1] + "." + s[i+1:], i + 2, needed - 1)
                return

            start = i
            maxCapacity = needed * 3
            for i in range(i, min(i+4, len(s) - 1)):
                # Exit early if there is not enough digits left to compelte a valid ip-address
                if len(s) - i - 1 > maxCapacity:
                    continue
                # Make sure value isn't too large.
                if int(s[start:i+1]) > 255:
                    continue
                dfs(s[:i+1] + "." + s[i+1:], i + 2, needed - 1)

        dfs(s, 0, 3)
        return res


s = "101023"
output = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

obj = Solution()
res = obj.restoreIpAddresses(s)
print(res)
print(output)
print(res == output)
