using System.Data;

class for반복문
{
    static void Main0(string[] args)
    {
        int i=0;
for ( ; ; )
{
  if (i < 1000)
  {
    Console.WriteLine("출력 " + i);
    i++;
  }
  else
  {
    break;
  }
}
    }
// do~while문을 for문으로 바꾸기
// string input;
// do
// {
// Console.Write("입력(exit을 입력하면 종료): ");
// input = Console.ReadLine();
// }while=Console.ReadLine();
// }

    static void Main1(string[] args)
    {
        string input;

        for (;;)
        {
            Console.Write("입력(exit을 입력하면 종료): ");
            input = Console.ReadLine();

            if (input == "exit")
                break;
        }
    }

    static void Main2(string[] args)
    {
        long start = DateTime.Now.Ticks;
        long count = 0;

        while(start + (10000000)> DateTime.Now.Ticks)
        {
            count++;
        }
        Console.WriteLine(count + "만큼 반복했습니다.");
    }
}