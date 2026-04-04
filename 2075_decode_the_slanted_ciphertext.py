class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n//rows
        res = ""
        for col in range(cols):
            for row in range(rows):
                i = (cols*row) + col + row
                if i < n:
                    res += encodedText[i]
        return res.rstrip()
