public class Solution
{
    public IList<IList<int>> Subsets(int[] nums)
    {
        IList<int> cur = [];
        IList<IList<int>> result = FindCombinations(-1, cur, nums);
        result.Add([]);
        return result;
    }

    public IList<IList<int>> FindCombinations(int l, IList<int> cur, int[] array)
    {
        IList<IList<int>> result = [];
        l++;
        while (l < array.Length)
        {
            IList<int> copy = new List<int>(cur)
            {
                array[l]
            };
            result.Add(copy);
            IList<IList<int>> temp = FindCombinations(l, copy, array);
            foreach (IList<int> arr in temp)
            {
                result.Add(arr);
            }
            l++;
        }
        return result;
    }
}