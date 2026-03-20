public class Solution {
    public int[][] MinAbsDiff(int[][] grid, int k) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int[][] res = new int[rows-k+1][];
        for(int row = 0; row<rows-k+1; row++){
            res[row] = new int[cols-k+1];
        }
        if(k == 1)
            return res;
        for(int row = 0; row<rows-k+1; row++){
            for(int col = 0; col<cols-k+1; col++){
                int min = int.MaxValue;
                int max = int.MinValue;
                int[] nums = new int[k*k];
                for(int i = row; i<row+k; i++){
                    for(int j = col; j<col+k; j++){

                        int idx = ((i-row)*k)+(j-col);
                        nums[idx] = grid[i][j];
                    }
                }
                int diff = int.MaxValue;
                Array.Sort(nums);
                for(int i = 1; i<k*k; i++){
                    if(nums[i]-nums[i-1] == 0)
                        continue;
                    diff = Math.Min(diff, nums[i]-nums[i-1]);
                }
                if(diff == int.MaxValue)
                    diff = 0;
                res[row][col] = diff;
            }
        }
        return res;
    }
}