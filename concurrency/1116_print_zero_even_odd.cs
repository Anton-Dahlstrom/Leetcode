using System.Threading;
public class ZeroEvenOdd
{
    private int n;
    private SemaphoreSlim zeroSem = new(1, 1);
    private SemaphoreSlim evenSem = new(0, 1);
    private SemaphoreSlim oddSem = new(0, 1);

    public ZeroEvenOdd(int n)
    {
        this.n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Zero(Action<int> printNumber)
    {
        for (int cnt = 1; cnt <= n; cnt++)
        {
            zeroSem.Wait();
            printNumber(0);
            if (cnt % 2 == 1)
            {
                oddSem.Release();
            }
            else
            {
                evenSem.Release();
            }
        }
    }

    public void Even(Action<int> printNumber)
    {
        for (int i = 2; i <= n; i += 2)
        {
            evenSem.Wait();
            printNumber(i);
            zeroSem.Release();
        }
    }

    public void Odd(Action<int> printNumber)
    {
        for (int i = 1; i <= n; i += 2)
        {
            oddSem.Wait();
            printNumber(i);
            zeroSem.Release();
        }
    }
}