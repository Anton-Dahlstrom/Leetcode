public class Solution
{
    public int MaxSideLength(int[][] mat, int threshold)
    {
        int rows = mat.Length;
        int cols = mat[0].Length;
        int res = 0;
        int cur;
        int side;
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                cur = 0;
                side = 1;
                while (CanExpand(row, col, side, rows, cols))
                {
                    cur += ExpansionCost(row, col, side, mat);
                    if (cur <= threshold)
                    {
                        res = Math.Max(side, res);
                        side++;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        return res;
    }
    public int ExpansionCost(int toprow, int leftcol, int sidelen, int[][] mat)
    {
        if (sidelen == 1)
            return mat[toprow][leftcol];
        int botrow = toprow + sidelen - 1;
        int rightcol = leftcol + sidelen - 1;
        int adding = 0;
        for (int col = leftcol; col <= rightcol; col++)
        {
            adding += mat[botrow][col];
        }
        for (int row = toprow; row < botrow; row++)
        {
            adding += mat[row][rightcol];
        }
        return adding;
    }
    public bool CanExpand(int row, int col, int sidelen, int maxrows, int maxcols)
    {
        return (row + sidelen <= maxrows && col + sidelen <= maxcols);
    }
}