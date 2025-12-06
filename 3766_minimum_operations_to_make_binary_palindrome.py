class Solution:
    def minOperations(self, nums: list[int]) -> list[int]:
        palindromes = {1}

        # Make all possible palindromes
        def dfs(cur):
            if len(cur) > 12:
                return
            palindromes.add(int("1"+cur+"1", 2))
            dfs("0" + cur + "0")
            dfs("1" + cur + "1")

        dfs("")
        dfs("0")
        dfs("1")
        palindromes = list(palindromes)
        palindromes.sort()
        res = []
        for num in nums:
            if num <= palindromes[0]:
                res.append(palindromes[0]-num)
                continue

            # find first palindrome that num is greater than, compare that and next num to palindrome.
            l, r = 0, len(palindromes)-1
            while l <= r:
                mid = l + ((r-l)//2)
                if palindromes[mid] > num:  # can't be this one, increase l
                    r = mid-1
                else:
                    l = mid+1
            res.append(min(num-palindromes[r], palindromes[r+1] - num))

        return res


nums = [6, 7, 12]
output = [1, 0, 3]

obj = Solution()
res = obj.minOperations(nums)
print(res)
print(output)
print(res == output)
