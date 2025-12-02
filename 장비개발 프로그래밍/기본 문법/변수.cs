class 변수
{
// 오버플로
// 2,147,483,647에 1을 더하면 int 자료형의 범위를 넘어버리면서 -2,147,483,648이 됨
    static void Main0(string[] args)
    {
        int a = 2147483640;
        int b = 52273;
        Console.WriteLine(a+b);
    }

    static void Main1(string[] args)
    {
        int a = 2147483640;
        int b = 52273;
        Console.WriteLine(a+b);
    }
    static void Main2(string[] args)
    {
        uint unsignedA = 200000000;
        uint unsignedB = 100000000;
        Console.WriteLine(unsignedA+unsignedB);
    }
// unsigned 자료형
// int 자료형은 -2147483648부터2147483647까지 나타낼 수 있음
// 음수를 사용하지 않는다면 -2147483648부터 -1까지의 숫자가 낭비됨
// 이런 낭비를 막고자 C#은 unsigned 자료형(부호가 없는 자료형)을 제공
// int와 long 키워드 대신 uint와 ulong 키워드를 사용    
    static void Main3(string[] args)
    {
        uint unsignedInt = 4147483647;
        ulong unsignedLong = 11223372036854775808;
        
        Console.WriteLine(unsignedInt);
        Console.WriteLine(unsignedLong);
    }
// 최댓값과 최솟값
    static void Main4(string[] args)
    {
        Console.WriteLine(int.MaxValue);
        Console.WriteLine(int.MinValue);
    }

    static void Main5(string[] args)
    {
        Console.WriteLine(long.MaxValue);
        Console.WriteLine(long.MinValue);
    }

// sizeof 연산자와 char 자료형의 크기
    static void Main6(string[] args)
    {
        Console.WriteLine("int: " + sizeof(int));
        Console.WriteLine("long: " + sizeof(long));
        Console.WriteLine("float: " + sizeof(float));
        Console.WriteLine("double: " + sizeof(double));
        Console.WriteLine("char: " + sizeof(char));
    }
}