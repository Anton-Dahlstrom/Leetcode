using System.Threading;

public class Foo
{
    private readonly object _lock = new();
    int state = 0;
    public Foo()
    {

    }

    public void First(Action printFirst)
    {
        lock (_lock)
        {
            printFirst();
            state = 1;
            Monitor.PulseAll(_lock);
        }
    }

    public void Second(Action printSecond)
    {
        lock (_lock)
        {
            while (state != 1)
                Monitor.Wait(_lock);

            printSecond();
            state = 2;
            Monitor.PulseAll(_lock);
        }
    }

    public void Third(Action printThird)
    {
        lock (_lock)
        {
            while (state != 2)
                Monitor.Wait(_lock);

            printThird();
            state = 3;
        }
    }
}