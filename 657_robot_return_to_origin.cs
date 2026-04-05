public class Solution
{
    public bool JudgeCircle(string moves)
    {
        int up = 0;
        int right = 0;
        foreach (var chr in moves)
        {
            switch (chr)
            {
                case 'U':
                    up++;
                    break;
                case 'D':
                    up--;
                    break;
                case 'L':
                    right++;
                    break;
                case 'R':
                    right--;
                    break;
            }
        }
        if (up == 0 && right == 0)
            return true;
        return false;
    }
}