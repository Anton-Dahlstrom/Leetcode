public class Solution
{
    public int[][] ConstructProductMatrix(int[][] grid)
    {
        int MOD = 12345;
        int n = grid.Length;
        int m = grid[0].Length;
        if (n * m == 1)
            return grid;
        int total = 1;
        int[][] res = new int[n][];
        for (int i = 0; i < n; i++)
        {
            res[i] = new int[m];
        }
        int[] prefix = new int[n * m];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                total = total * (grid[i][j] % MOD) % MOD;
                prefix[(i * m) + j] = total;
            }
        }
        int[] suffix = new int[n * m];
        total = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = m - 1; j >= 0; j--)
            {
                total = total * (grid[i][j] % MOD) % MOD;
                suffix[(i * m) + j] = total;
            }
        }
        for (int i = 1; i < (n * m) - 1; i++)
        {
            res[i / m][i % m] = prefix[i - 1] * suffix[i + 1] % MOD;
        }
        res[0][0] = suffix[1] % MOD;
        res[n - 1][m - 1] = prefix[(n * m) - 2] % MOD;
        return res;
    }
}