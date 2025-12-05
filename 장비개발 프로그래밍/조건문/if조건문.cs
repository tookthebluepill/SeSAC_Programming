class if조건문
{
// 숫자 홀짝 판별
static void Main0(string[] args)
{
    Console.Write("숫자 입력:");
    int input = int.Parse(Console.ReadLine());

    if (input % 2 == 0)
    {
        Console.WriteLine("짝수입니다!");
    }
    
    if(input % 2 == 1)
    {
        Console.WriteLine("홀수입니다!");
    }

}
// 입력 받아 조건 분할
static void Main1(string[] args)
    {
        Console.Write("입력: ");
        String? line = Console.ReadLine();
        if(line.Contains("안녕"))
        {
            Console.WriteLine("안녕하세요...!");
        }
        else
        {
            Console.WriteLine("^^");
        }
    }
}