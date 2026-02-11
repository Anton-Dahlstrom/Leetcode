public class Solution {
    public int FinalElement(int[] nums) {
        int n = nums.Length;
        int a = nums[0];
        int b = nums[n-1];
        return Math.Max(a,b);
    }
}