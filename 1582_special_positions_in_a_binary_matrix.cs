public class Solution {
    public int NumSpecial(int[][] mat) {
        int res = 0;
        int rows = mat.Length;
        int cols = mat[0].Length;
        int[] rowcnt = new int[rows];
        int[] colcnt = new int[cols];
        for(int row = 0; row<rows; row++){
            for(int col = 0; col<cols; col++){
                if(mat[row][col] == 1){
                    rowcnt[row]++;
                    colcnt[col]++;
                }
            }
        }
        for(int row = 0; row<rows; row++){
            for(int col = 0; col<cols; col++){
                if(mat[row][col] == 1 && rowcnt[row] == 1 && colcnt[col] == 1){
                    res++;
                }
            }
        }
        return res;
    }
}