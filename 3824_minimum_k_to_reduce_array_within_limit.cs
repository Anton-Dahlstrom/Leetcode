public class Solution {
    public int MinimumK(int[] nums) {
        long l = 1;
        long r = 10000;
        if(r <= 0)
            return 0;
        while(l <= r){
            long mid = l+((r-l)/2);
            if(BruteForce(nums, mid))
                r = mid-1;
            else
                l = mid+1;
        }
        return (int)r+1;
    }
    public bool BruteForce(int[] nums, long k){
        long ops = 0;
        for(int i = 0; i<nums.Length; i++){
            ops += (nums[i] + k - 1) / k;
            if(ops>k*k)
                return false;
        }
        return true;
    }
}