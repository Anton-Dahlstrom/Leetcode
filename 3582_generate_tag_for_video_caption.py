import re


class Solution:
    def generateTag(self, caption: str) -> str:
        caption = re.sub(r'[^ a-zA-Z]', "", caption)
        caption.strip()
        caption = caption.split(" ")
        for i in range(len(caption)):
            if not caption[i]:
                continue
            caption[i] = caption[i].lower()
            if i:
                caption[i] = chr(ord(caption[i][0])-32) + caption[i][1:]

        return "#" + "".join(caption)[:99]


caption = "Leetcode daily streak achieved"
output = "#leetcodeDailyStreakAchieved"


obj = Solution()
res = obj.generateTag(caption)
print(res)
print(output)
print(res == output)
