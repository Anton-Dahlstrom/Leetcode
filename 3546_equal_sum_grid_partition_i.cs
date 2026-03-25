public class Solution
{
    public bool CanPartitionGrid(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int[] rowsum = new int[rows];
        int[] rowmod = new int[rows];
        int[] colsum = new int[cols];
        int[] colmod = new int[cols];
        int MOD = 100000;
        for (int row = rows - 1; row >= 0; row--)
        {
            for (int col = cols - 1; col >= 0; col--)
            {
                rowsum[row] += grid[row][col];
                rowmod[row] += rowsum[row] / MOD;
                rowsum[row] %= MOD;

                colsum[col] += grid[row][col];
                colmod[col] += colsum[col] / MOD;
                colsum[col] %= MOD;

            }
        }
        if (rows > 1)
        {
            int l = 1;
            int lsum = rowsum[0];
            int lmod = rowmod[0];
            int r = rows - 2;
            int rsum = rowsum[rows - 1];
            int rmod = rowmod[rows - 1];
            while (r >= l)
            {
                if (rmod < lmod | (rmod == lmod && rsum < lsum))
                {
                    rsum += rowsum[r];
                    rmod += rsum / MOD;
                    rsum %= MOD;
                    rmod += rowmod[r];
                    r--;
                }
                else
                {
                    lsum += rowsum[l];
                    lmod += lsum / MOD;
                    lsum %= MOD;
                    lmod += rowmod[l];
                    l++;
                }
            }
            if (rmod == lmod && rsum == lsum)
                return true;
        }
        if (cols > 1)
        {
            int l = 1;
            int lsum = colsum[0];
            int lmod = colmod[0];
            int r = cols - 2;
            int rsum = colsum[cols - 1];
            int rmod = colmod[cols - 1];
            while (r >= l)
            {
                if (rmod < lmod | (rmod == lmod && rsum < lsum))
                {
                    rsum += colsum[r];
                    rmod += rsum / MOD;
                    rsum %= MOD;
                    rmod += colmod[r];
                    r--;
                }
                else
                {
                    lsum += colsum[l];
                    lmod += lsum / MOD;
                    lsum %= MOD;
                    lmod += colmod[l];
                    l++;
                }
            }
            if (rmod == lmod && rsum == lsum)
                return true;
        }
        return false;
    }
}