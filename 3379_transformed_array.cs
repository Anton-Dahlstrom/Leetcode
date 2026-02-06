public class Solution {
    public int[] ConstructTransformedArray(int[] nums) {
        int n = nums.Length;
        var res = new int[n];
        for(int i = 0; i<n; i++){
            int index = (i + nums[i]) % n;
            if(index >= 0)
                res[i] = nums[index];
            else{
                index = Math.Abs(index);
                res[i] = nums[^index];
            }
        }
        return res;
    }
}