public class Solution
{
    public int BulbSwitch(int n)
    {
        int i = 1;
        HashSet<int> hset = new();
        while (i * i <= n)
        {
            int cur = i * i;
            hset.Add(cur);
            i++;
        }
        return hset.Count;
    }
}