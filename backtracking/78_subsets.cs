public class Solution
{
    public IList<IList<int>> Subsets(int[] nums)
    {
        IList<IList<int>> result = [];
        result.Add(nums);
        int l = 0;
        while (l < nums.Length)
        {
            int[] temp = [];
            break;

        }

        for (int i = 0; i < result.Count; i++)
        {
            Console.WriteLine(string.Join(" ", result[i]));
        }
        return result;
    }
}