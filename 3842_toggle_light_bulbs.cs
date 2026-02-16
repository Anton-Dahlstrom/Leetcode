public class Solution
{
    public IList<int> ToggleLightBulbs(IList<int> bulbs)
    {
        List<int> state = new List<int>(new int[101]);
        for (int i = 0; i < bulbs.Count; i++)
        {
            state[bulbs[i]] = Math.Abs(state[bulbs[i]] - 1);
        }
        List<int> res = new();
        for (int i = 0; i < state.Count; i++)
        {
            if (state[i] == 1)
                res.Add(i);
        }
        return res;
    }
}