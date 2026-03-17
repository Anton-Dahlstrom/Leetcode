public class Solution
{
    public int LargestSubmatrix(int[][] matrix)
    {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[][] prefix = new int[rows][];
        for (int row = 0; row < rows; row++)
        {
            prefix[row] = new int[cols];
        }
        for (int col = 0; col < cols; col++)
        {
            int cur = 0;
            for (int row = rows - 1; row >= 0; row--)
            {
                if (matrix[row][col] == 1)
                    cur++;
                else
                    cur = 0;
                prefix[row][col] = cur;
            }
        }
        foreach (var col in prefix)
        {
            Array.Sort(col);
            Array.Reverse(col);
        }
        int res = 0;
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                res = Math.Max(res, (col + 1) * prefix[row][col]);
            }
        }
        return res;
    }
}