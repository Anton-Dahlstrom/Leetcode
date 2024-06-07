from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            print("hi")
            return
        if len(strs) == 1 and strs[0] == "":
            return ""
        return " # ".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            if type(s) == str:
                return [""]
            return []
        return s.split(" # ")
