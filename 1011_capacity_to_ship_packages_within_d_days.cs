public class Solution
{
    public int ShipWithinDays(int[] weights, int days)
    {
        int left = 0;
        int right = weights.Sum();
        int mid;
        while (left <= right)
        {
            mid = left + ((right - left) / 2);
            if (CanShip(weights, days, mid))
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return right + 1;
    }
    public bool CanShip(int[] weights, int days, int capacity)
    {
        int curdays = 0;
        int cur = 0;
        foreach (var weight in weights)
        {
            if (weight > capacity || curdays > days)
                return false;
            if (cur + weight > capacity)
            {
                cur = 0;
                curdays++;
            }
            cur += weight;
        }
        return curdays + 1 <= days;
    }
}