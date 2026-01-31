public class Solution
{
    public char NextGreatestLetter(char[] letters, char target)
    {
        foreach (var c in letters)
        {
            if (c > target)
                return c;
        }
        return letters[0];
    }
}