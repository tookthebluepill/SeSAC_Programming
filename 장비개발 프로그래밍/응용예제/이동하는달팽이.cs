using System;
using System.Threading;

class 움직이는달팽이
{
    static void Main0(string[] args)
{
    int x = 1;
    while (x<50)
        {
            //화면을 지우고 커서를 이동
            Console.Clear();
            Console.SetCursorPosition(x,5);

            //출력
            if(x%3==0)
            Console.WriteLine("__@");
            else if (x%3==1)
            Console.WriteLine("_^@");
            else
            Console.WriteLine("^_@");
            Thread.Sleep(100);
            x++;
        }
}
}