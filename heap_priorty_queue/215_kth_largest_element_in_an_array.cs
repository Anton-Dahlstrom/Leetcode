using System.Globalization;

public class MaxHeap
{
    public void Heapify(int[] array)
    {
        for (int i = array.Length - 1; i >= 0; i--)
        {
            MoveUp(array, i);
        }
    }
    public void MoveUp(int[] array, int child)
    {
        int parent = (child - 1) / 2;
        while (child > 0 && parent >= 0 && array[child] > array[parent])
        {
            (array[child], array[parent]) = (array[parent], array[child]);
            child = parent;
            parent = (child - 1) / 2;
        }
    }
    public void MoveDown(int[] array, int parent)
    {
        int len = array.Length;
        int child;
        int child1 = parent * 2 + 1;
        int child2 = parent * 2 + 2;
        while ((child2 < len && array[parent] < array[child2])
        || (child1 < len && array[parent] < array[child1]))
        {
            if (child2 < len)
            {
                if (array[child1] < array[child2])
                {
                    child = child1;
                }
                else { child = child2; }
            }
            else { child = child1; }
            (array[child], array[parent]) = (array[parent], array[child]);
            parent = child;
            child1 = parent * 2 + 1;
            child2 = parent * 2 + 2;
        }
    }
}

public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        MaxHeap heap = new MaxHeap();
        heap.Heapify(nums);

        // Compare all the child-nodes to find the next largest number.
        // Add the index of the largest node to parents while keeping track of 
        // the children you've checked.
        // Each time you add a value to the parent array subtract 1 from k until k = 0
        // The value of the last addition is the k largest number.
        int cur = int.MinValue;
        int parent = 0;
        int child1;
        int child2;
        List<int> nodes = new List<int>();
        int result = nums[0];

        while (k > 1)
        {
            child1 = parent * 2 + 1;
            if (child1 < nums.Length)
            {
                nodes.Add(child1);
            }
            child2 = parent * 2 + 2;
            if (child2 < nums.Length)
            {
                nodes.Add(child2);
            }
            int value;
            int index;
            int remove = 0;
            for (int i = 0; i < nodes.Count; i++)
            {
                index = nodes[i];
                value = nums[index];
                if (value > cur)
                {
                    cur = value;
                    parent = index;
                    remove = i;
                }
            }
            result = cur;
            Console.WriteLine(result);
            cur = int.MinValue;
            nodes.RemoveAt(remove);
            k--;
        }
        return result;
    }
}