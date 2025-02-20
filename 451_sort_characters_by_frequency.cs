public class Solution
{
    public string FrequencySort(string s)
    {
        Dictionary<char, int> count = [];
        foreach (char chr in s)
        {
            count[chr] = count.GetValueOrDefault(chr, 0) + 1;
        }
        var test = count.ToList();
        test.Sort((kv1, kv2) => kv2.Value.CompareTo(kv1.Value));

        string res = "";
        foreach (var t in test)
        {
            res += new string(t.Key, t.Value);
        }
        return res;
    }
}
