using System.Globalization;

class homework2
{
// 숫자를 입력받아 입력한 숫자(단)의 구구단 출력
// 단을 입력해주세요
// 단: 

    static void Main0(string[] args)
    {
        Console.WriteLine("단을 입력해주세요");
        Console.Write("단:");
        string? input = Console.ReadLine();
        int dan = int.Parse(input);
        for (int i=1 ; i< 10; i++)
        {
            int j = dan * i;
            Console.WriteLine($"{dan} * {i} = {j}");
        }
    }

// 1에서 20까지의 정수에서 2의 배수와 3의 배수를 제외한 숫자를 출력
    static void Main(string[] args)
    {
        for (int i = 1; i <= 20; i++)
        {
            if (i % 2 != 0 && i % 3 != 0)
            {
                Console.WriteLine(i);
            }
        }
    }
}