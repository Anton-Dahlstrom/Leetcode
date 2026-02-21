public class Solution
{
    public int CountPrimeSetBits(int left, int right)
    {
        int res = 0;
        int cur;
        int nxt;
        int cnt;
        for (int i = left; i <= right; i++)
        {
            cnt = 0;
            cur = i;
            while (cur > 0)
            {
                nxt = cur;
                nxt >>= 1;
                nxt <<= 1;
                if (cur != nxt)
                {
                    cnt++;
                }
                cur >>= 1;
            }
            if (IsPrime(cnt))
            {
                res++;
            }
        }
        return res;
    }
    public bool IsPrime(int num)
    {
        if (num <= 1)
        {
            return false;
        }
        for (int i = 2; i <= num / 2; i++)
        {
            if (num % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}