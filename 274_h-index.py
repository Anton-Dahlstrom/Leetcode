class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        l, r = 0, len(citations)-1
        mid = 0
        while l <= r:
            mid = l + ((r-l)//2)

            if citations[mid] < mid+1:
                r = mid-1
            else:
                l = mid +1
        if citations[mid] < mid+1:
            mid -=1
        return mid+1

citations = [3,0,6,1,5]
output= 3 

obj = Solution()
res = obj.hIndex(citations)
print(res)
print(output)
print(res == output)