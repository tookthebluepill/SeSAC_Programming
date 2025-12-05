class 조건연산자
{
    static void Main0(string[] args)
    {
        string input = Console.ReadLine();
        int number = int.Parse(input);
        Console.WriteLine(number > 0 ? "자연수입니다" : "자연수가 아닙니다");
    }
}