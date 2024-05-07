// Count how many tasks each character needs.
// Create sorted list and execute a task with the most tasks left that is available.
// Track the character, how many tasks still needs to be done and the last cycle it was executed
// in a class. 
// Count how many turns are used and return answer.

public class Tasks
{
    public char key;
    public int val;
    public int cycle;
    public Tasks(char letter, int value)
    {
        key = letter;
        val = value;
        cycle = int.MinValue;
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
        List<Tasks> stack = new List<Tasks>();

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
            stack.Insert(i, new Tasks(key, hmap[key]));
        }
        int cycle = 0;
        // Runs while the stack still has uncompleted tasks.
        while (stack.Count > 0)
        {
            cycle++;
            // Looks for a task that can be done in the stack.
            for (i = 0; i < stack.Count; i++)
            {
                if (stack[i].cycle + n < cycle)
                {
                    stack[i].val -= 1;
                    stack[i].cycle = cycle;
                    for (i++; i < stack.Count; i++)
                    {
                        if (stack[i - 1].val < stack[i].val)
                        {
                            (stack[i], stack[i - 1]) = (stack[i - 1], stack[i]);
                        }
                        else { break; }
                    }
                    if (stack.Count > 0 && stack[stack.Count - 1].val < 1)
                    {
                        stack.RemoveAt(stack.Count - 1);
                    }
                    break;
                }
            }
        }
        return cycle;
    }
}