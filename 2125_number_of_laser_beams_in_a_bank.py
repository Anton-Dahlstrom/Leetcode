class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            cur = row.count("1")
            if cur:
                res += prev*cur
                prev = cur
        return res


bank = ["011001", "000000", "010100", "001000"]
output = 8

obj = Solution()
res = obj.numberOfBeams(bank)
print(res)
print(output)
print(res == output)
