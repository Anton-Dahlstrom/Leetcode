public class Solution {
    public int LongestSubsequence(int[] nums) {
        int res = 0;
        int i = 0;
        int bit = 2;
        double maxsize = Math.Pow(10,9);
        while(bit <= maxsize){
            bit = (int)Math.Pow(2,i);
            res = Math.Max(res, CountIncWithBit(bit, nums));
            i++;
        }
        return res;
    }
    public int CountIncWithBit(int bit, int[] nums){
        List<int> list = new();
        for(int i = 0; i<nums.Length; i++){
            if((bit & nums[i]) == 0)
                continue;
            if(list.Count == 0 || nums[i] > list[^1]){
                list.Add(nums[i]);
            }
            else{
                int index = LowerBoundBinarySearch(list, nums[i]);
                list[index] = nums[i];
            }
        }
        return list.Count;
    }
    public int LowerBoundBinarySearch(List<int> list, int value){
        int l = 0;
        int r = list.Count-1;
        int mid;
        while(l <= r){
            mid = l+((r-l)/2);
            if(list[mid] >= value){
                r = mid-1;
            }
            else{
                l = mid+1;
            }
        }
        return r+1;
    }
}