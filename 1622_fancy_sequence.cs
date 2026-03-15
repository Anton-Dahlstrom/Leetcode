public class Fancy
{
    // val, i
    private List<List<int>> nums = new();
    // 0 = add, 1 = mult
    private List<List<int>> stack = new();
    private int i = 0;
    private int MOD = (int)Math.Pow(10, 9) + 7;
    public Fancy()
    {

    }

    public void Append(int val)
    {
        this.nums.Add(new List<int>() { val, this.i });
    }

    public void AddAll(int inc)
    {
        stack.Add(new List<int>() { 0, inc });
        this.i++;
    }

    public void MultAll(int m)
    {
        stack.Add(new List<int>() { 1, m });
        this.i++;
    }

    public int GetIndex(int idx)
    {
        if (idx >= nums.Count)
        {
            return -1;
        }
        // val, index
        List<int> cur = this.nums[idx];
        while (cur[1] < this.stack.Count)
        {
            if (this.stack[cur[1]][0] == 0)
            {
                cur[0] = (int)((cur[0] + (long)this.stack[cur[1]][1]) % this.MOD);
            }
            else
            {
                cur[0] = (int)((cur[0] * (long)this.stack[cur[1]][1]) % this.MOD);
            }
            cur[1]++;
        }
        return (int)cur[0];
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * int param_4 = obj.GetIndex(idx);
 */