// Count how many tasks each character needs.
// Create sorted list and execute a task with the character with most tasks left that's available.
// Use something to keep track of which chars are unavailable.
// Count how many turns are used and return answer.
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
        List<KeyValuePair<char, int>> stack = new List<KeyValuePair<char, int>>();
        foreach (char key in hmap.Keys)
        {
            Console.WriteLine(key);
            Console.WriteLine(hmap[key]);
            stack.Add(new KeyValuePair<char, int>(key, hmap[key]));
        }
        foreach (KeyValuePair<char, int> kvp in stack)
        {
            Console.WriteLine($"{kvp.Key} {kvp.Value}");
        }
        return 0;
    }
}