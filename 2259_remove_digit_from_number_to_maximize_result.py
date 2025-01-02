class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        remove = 0
        for i in range(len(number)):
            if number[i] == digit:
                remove = i
                if i < len(number) - 1 and int(number[i+1]) > int(digit):
                    break
        return number[0:remove] + number[remove+1:]


number = "123"
digit = "3"
output = "12"


obj = Solution()
res = obj.removeDigit(number, digit)
print(res)
print(output)
print(res == output)
