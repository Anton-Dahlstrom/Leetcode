
public class Solution
{
    IList<int> temp = [];
    IList<IList<int>> result = [];
    int[] candidates = [];
    public IList<IList<int>> CombinationSum(int[] candidates, int target)
    {
        Array.Sort(candidates);
        this.candidates = candidates;
        Search(0, target, 0);
        return result;
    }

    public void Search(int i, int target, int sum)
    {
        if (i >= candidates.Length || sum > target)
        {
            return;
        }

        if (sum == target)
        {
            IList<int> copy = new List<int>(temp);
            result.Add(copy);
            return;
        }

        temp.Add(candidates[i]);
        sum += candidates[i];
        Search(i + 0, target, sum);
        if (temp.Count > 0)
        {
            temp.RemoveAt(temp.Count - 1);
        }
        sum -= candidates[i];
        Search(i + 1, target, sum);

        return;
    }
}