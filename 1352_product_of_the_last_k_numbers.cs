public class ProductOfNumbers
{
    List<int> Prefix = []
        public ProductOfNumbers()
    {
        List<int> prefix = [];
    }

    public void Add(int num)
    {
        if (num == 0)
        {
            Prefix = [];
        }
        else
        {
            Prefix.Add(num);
            if (Prefix.Count > 1)
            {
                Prefix[Prefix.Count -
                    1] *= Prefix[Prefix.Count - 2];
            }

        }
    }

    public int GetProduct(int k)
    {
        // Console.WriteLine($"COUNT: {Prefix.Count}");
        if (k > Prefix.Count)
        {
            return 0;
        }
        else
        {
            int res = Prefix[Prefix.Count - 1];
            if (k < Prefix.Count)
            {
                res /= Prefix[Prefix.Count - 1 - k];
            }
            return res;
        }
    }
}

/**
    * Your ProductOfNumbers object will be instantiated and called as such:
    * ProductOfNumbers obj = new ProductOfNumbers()
    * obj.Add(num)
    * int param_2 = obj.GetProduct(k)
    */
internal class Program
{
    static void Main(string[] args)
    {
        ProductOfNumbers obj = new()
        List<string> input = ["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"];
        List<List<int>> values = [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]];
        List<int?> output = [null];
        for (int i = 1; i < values.Count; i + +)
        {
            string command = input[i];
            int val = values[i][0];
            if (command == "add")
            {
                obj.Add(val);
            }
            else if (command == "getProduct")
            {
                output.Add(obj.GetProduct(val));
                continue;
            }
            output.Add(null);
        }
        string res = "[" + string.Join(", ", output.Select(n = > n?.ToString() ?? "null")) + "]";
        Console.WriteLine(res);
    }
}
