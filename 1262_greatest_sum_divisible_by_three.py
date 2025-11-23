class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        res = sum(nums)
        remainder = res % 3
        ones = []
        twos = []
        for num in nums:
            if num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)
        ones.sort(reverse=True)
        twos.sort(reverse=True)
        best = res
        if not remainder:
            return res

        if remainder == 1:
            if ones:
                best = min(best, ones[-1])
            if len(twos) >= 2:
                best = min(best, sum(twos[-2:]))
        elif remainder == 2:
            if len(ones) >= 2:
                best = min(best, sum(ones[-2:]))
            if twos:
                best = min(best, twos[-1])

        return res-best


nums = [3, 6, 5, 1, 8]
output = 18

nums = [1, 2, 3, 4, 4]
output = 12

nums = [5, 2, 2, 2]
output = 9

nums = [366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984, 787, 552, 14, 545,
        866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]
output = 50487

nums = [4, 1, 5, 3, 1]
output = 12

obj = Solution()
res = obj.maxSumDivThree(nums)
print(res)
print(output)
print(res == output)
