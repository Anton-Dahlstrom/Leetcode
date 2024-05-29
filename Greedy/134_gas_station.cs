// Slow but memory efficient solution that iterates through each starting index and checks if it can make it back.
public class Solution
{
    public int CanCompleteCircuit(int[] gas, int[] cost)
    {
        int cur = 0;
        int start;
        int i = 0;
        for (start = 0; start < gas.Length; start++)
        {
            i = start;
            cur = gas[i];
            do
            {
                cur -= cost[i];
                if (i >= gas.Length - 1)
                {
                    i = 0;
                }
                else { i++; }


                if (cur <= 0)
                {
                    break;
                }
                if (i != start)
                {
                    cur += gas[i];
                }

            } while (i != start);
            if (cur > 0 || (cur == 0 && i == start))
            {
                return i;
            }

        }
        return -1;
    }
}