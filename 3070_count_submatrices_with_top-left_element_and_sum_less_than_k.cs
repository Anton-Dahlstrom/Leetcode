public class Solution
{
    public int CountSubmatrices(int[][] grid, int k)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int[][] prefix = new int[rows][];
        int res = 0;
        for (int row = 0; row < rows; row++)
        {
            prefix[row] = new int[cols];
            int colsum = 0;
            for (int col = 0; col < cols; col++)
            {
                colsum += grid[row][col];
                prefix[row][col] = colsum;
                if (row > 0)
                {
                    prefix[row][col] += prefix[row - 1][col];
                }
                if (prefix[row][col] <= k)
                {
                    res++;
                }
            }
        }
        return res;
    }
}