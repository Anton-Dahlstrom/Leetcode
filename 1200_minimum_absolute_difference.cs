public class Solution
{
    public IList<IList<int>> MinimumAbsDifference(int[] arr)
    {
        Array.Sort(arr);
        List<IList<int>> res = new List<IList<int>>();
        int mindiff = int.MaxValue;
        for (int i = 0; i < arr.Length - 1; i++)
        {
            int diff = Math.Abs(arr[i] - arr[i + 1]);
            if (diff < mindiff)
            {
                mindiff = diff;
                res = new List<IList<int>>();
            }
            if (diff == mindiff)
                res.Add(new List<int> { arr[i], arr[i + 1] });
        }
        return res;
    }
}