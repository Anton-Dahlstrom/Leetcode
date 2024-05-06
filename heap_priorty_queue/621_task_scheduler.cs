// Count how many tasks each character needs.
// Create sorted list and execute a task with the character with most tasks left that's available.
// Use something to keep track of which chars are unavailable.
// Count how many turns are used and return answer.

public class ValueClass
{
    public char key;
    public int val;
    public int task;
    public ValueClass(char letter, int value)
    {
        key = letter;
        val = value;
        task = int.MinValue;
    }
}

public class Solution
{
    public int LeastInterval(char[] tasks, int n)
    {
        Dictionary<char, int> hmap = new Dictionary<char, int>();
        foreach (char key in tasks)
        {
            if (hmap.ContainsKey(key))
            {
                hmap[key]++;
            }
            else
            {
                hmap.Add(key, 1);
            }
        }
        List<ValueClass> stack = new List<ValueClass>();

        int i;
        foreach (char key in hmap.Keys)
        {
            for (i = 0; i < stack.Count(); i++)
            {
                if (hmap[key] > stack[i].val)
                {
                    break;
                }
            }
            stack.Insert(i, new ValueClass(key, hmap[key]));
        }

        int task = 0;
        while (stack.Count > 0)
        {
            task++;
            for (i = 0; i < stack.Count; i++)
            {
                if (stack[i].task < task + n)
                {
                    stack[i].val -= 1;
                    stack[i].task = task;
                    for (i++; i < stack.Count; i++)
                    {
                        if (stack[i - 1].val < stack[i].val)
                        {
                            (stack[i], stack[i - 1]) = (stack[i - 1], stack[i]);
                        }
                        else { break; }
                    }
                }
                if (stack.Count > 0 && stack[stack.Count - 1].val < 1)
                {
                    stack.RemoveAt(stack.Count - 1);
                }
            }
        }
        Console.WriteLine(task);
        return task;
    }
}