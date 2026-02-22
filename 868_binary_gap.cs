public class Solution
{
    public int BinaryGap(int n)
    {
        int temp;
        int res = 0;
        int cnt = 0;
        bool first = false;
        int i = 0;
        while (n >> i > 0)
        {
            i++;
            temp = n;
            n >>= i;
            n <<= i;
            if (n == temp)
            {
                cnt++;
            }
            else
            {
                if (first == true)
                {
                    res = Math.Max(res, cnt);
                }
                first = true;
                cnt = 1;
            }
        }
        return res;
    }
}