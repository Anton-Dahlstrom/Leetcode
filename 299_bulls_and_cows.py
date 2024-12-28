class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        opensecret = {}
        openguess = {}
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
                continue

            if secret[i] in openguess and openguess[secret[i]] > 0:
                openguess[secret[i]] -= 1
                cows += 1
            else:
                opensecret.setdefault(secret[i], 0)
                opensecret[secret[i]] += 1

            if guess[i] in opensecret and opensecret[guess[i]] > 0:
                opensecret[guess[i]] -= 1
                cows += 1
            else:
                openguess.setdefault(guess[i], 0)
                openguess[guess[i]] += 1
        return str(bulls) + "A" + str(cows) + "B"


secret = "1807"
guess = "7810"
output = "1A3B"

obj = Solution()
res = obj.getHint(secret, guess)
print(res)
print(output)
print(res == output)
