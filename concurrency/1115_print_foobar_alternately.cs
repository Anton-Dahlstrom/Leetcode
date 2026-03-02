using System.Threading;
public class FooBar
{
    private int n;
    private readonly SemaphoreSlim fooSemaphore = new(1, 1);
    private readonly SemaphoreSlim barSemaphore = new(0, 1);

    public FooBar(int n)
    {
        this.n = n;
    }

    public void Foo(Action printFoo)
    {

        for (int i = 0; i < n; i++)
        {
            fooSemaphore.Wait();
            printFoo();
            barSemaphore.Release();
        }
    }

    public void Bar(Action printBar)
    {

        for (int i = 0; i < n; i++)
        {
            barSemaphore.Wait();
            printBar();
            fooSemaphore.Release();
        }
    }
}